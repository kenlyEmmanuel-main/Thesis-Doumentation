#!/usr/bin/env python3
"""Build the full thesis or a full-context chapter/reference preview."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = {
    "chapter1": "chapters/ch1_intro",
    "chapter2": "chapters/ch2_lit_review",
    "chapter3": "chapters/ch3_methodology",
}


def run(command, *, cwd, env=None):
    print("+", subprocess.list2cmdline([str(arg) for arg in command]), flush=True)
    subprocess.run([str(arg) for arg in command], cwd=cwd, env=env, check=True)


def publish(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Stage beside the destination so the final replace is atomic, even when the
    # system temporary directory is on a different filesystem.
    with tempfile.NamedTemporaryFile(dir=destination.parent, suffix=".pdf", delete=False) as staged:
        staged_path = Path(staged.name)
        try:
            with source.open("rb") as pdf:
                shutil.copyfileobj(pdf, staged)
        except BaseException:
            staged_path.unlink(missing_ok=True)
            raise
    try:
        try:
            os.replace(staged_path, destination)
        except PermissionError as exc:
            raise PermissionError(
                f"Cannot replace {destination}. Close it in PDF viewers and retry."
            ) from exc
    finally:
        staged_path.unlink(missing_ok=True)


def build(target):
    with tempfile.TemporaryDirectory(prefix="thesis-build-") as temp:
        work = Path(temp)
        # LaTeX writes one aux file for each \include under the output directory.
        (work / "chapters").mkdir()
        latex = [
            "pdflatex", "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", "-jobname=main", f"-output-directory={work}",
        ]
        run([*latex, "main.tex"], cwd=ROOT)
        env = os.environ.copy()
        # Preserve the TeX distribution's default search paths after the project.
        env["BIBINPUTS"] = str(ROOT) + os.pathsep + env.get("BIBINPUTS", "")
        run(["bibtex", "main"], cwd=work, env=env)
        run([*latex, "main.tex"], cwd=ROOT)
        run([*latex, "main.tex"], cwd=ROOT)
        if target == "full":
            destination = ROOT / "main.pdf"
        else:
            selected = CHAPTERS.get(target, "")
            chapter_flag = "\\def\\thesischapterpreview{1}" if target in CHAPTERS else ""
            preview = (
                "\\def\\thesispreview{1}"
                f"\\def\\thesisinclude{{{selected}}}"
                f"{chapter_flag}"
                "\\input{main.tex}"
            )
            # Reuse the full manuscript's aux and bibliography for numbering.
            run([*latex, preview], cwd=ROOT)
            destination = ROOT / "build" / "previews" / f"{target}.pdf"
        publish(work / "main.pdf", destination)

        print(f"Wrote {destination}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", choices=("full", *CHAPTERS, "references"))
    args = parser.parse_args()
    try:
        build(args.target)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
