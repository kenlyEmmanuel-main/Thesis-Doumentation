# Capstone / Thesis Research Documentation ($\LaTeX$)

This repository contains the official modular $\LaTeX$ source files for our Capstone / Thesis manuscript, configured according to the **Ateneo de Naga University (ADNU) ECE and CpE Department Writing Guidelines** (`072211-Writing-guidelines-revised (1).pdf`).

---

## 1. Quick Start Prerequisites (What You Need to Install)

To clone, edit, compile, and preview this paper on your local machine, install the following tools:

### Step 1: Install Git
- **Windows / macOS / Linux:** Download and install [Git](https://git-scm.com/downloads).
- Verify in terminal:
  ```bash
  git --version
  ```

### Step 2: Install a $\LaTeX$ Distribution Engine
You need a local $\TeX$ distribution that provides `pdflatex` and `bibtex`.

- **Windows (Recommended):** Download and install [MiKTeX](https://miktex.org/download) (64-bit).
  - *Important during installation:* Choose **"Always install missing packages on-the-fly"** (or set to "Yes") so required packages install automatically during your first compile.
  - Verify in command prompt:
    ```bash
    pdflatex --version
    bibtex --version
    ```
- **macOS:** Install MacTeX via Homebrew or installer:
  ```bash
  brew install --cask mactex
  ```
- **Linux (Ubuntu/Debian):** Install the full TeX Live suite:
  ```bash
  sudo apt update && sudo apt install texlive-full
  ```
The build tasks also require Python 3.8 or later; verify with `python --version`.


### Step 3: Install the Editor / IDE
- Download and install **Antigravity IDE** (or [Visual Studio Code](https://code.visualstudio.com/)).

### Step 4: Install Required Editor Extension
- Open Antigravity IDE / VS Code.
- Go to the **Extensions** view (`Ctrl + Shift + X`).
- Search for and install:
  - **LaTeX Workshop** (by James Yu, ID: `James-Yu.latex-workshop`).

---

## 2. Workspace Setup

### 1. Clone the Repository
Open your terminal or Git Bash and clone the repository:
```bash
git clone https://github.com/kenlyEmmanuel-main/Thesis-Doumentation.git
cd "Thesis-Doumentation"
```

### 2. Open in Antigravity IDE / VS Code
Open the project root folder in your editor (`File` $\rightarrow$ `Open Folder...`).

### 3. Build Tasks
Auto-build is disabled so multiple compilations cannot overwrite one another.
Use **Terminal → Run Task** and select `Thesis: Build full`, `Thesis: Build chapter 1`,
`Thesis: Build chapter 2`, `Thesis: Build chapter 3`, or `Thesis: Build references`.
The full task is also available with `Ctrl+Shift+B`.
Builds use `pdflatex → bibtex → pdflatex → pdflatex`; PDFs can be opened in the editor.
Chapter previews refresh full-document reference data first, so their chapter,
equation, and citation numbers match the current full manuscript.
Links to content outside a chapter may not work in that chapter's standalone PDF.
Preview PDFs are written to `build/previews/chapter1.pdf`, `chapter2.pdf`,
`chapter3.pdf`, and `references.pdf`; the full build writes `main.pdf`.
You can also run `python scripts/build.py chapter1` (or `full`, `chapter2`,
`chapter3`, `references`) in a terminal at the project root. Temporary build
files are kept outside the project and removed automatically.
If Windows reports that a PDF cannot be replaced, close that PDF in all viewers
and rerun the task.
Each preview task overwrites its previous PDF. Preview PDFs in `build/` are
ignored by Git; the chapter `.tex` sources are tracked, and `main.pdf` is tracked.
The full build can report `Underfull` or `Overfull` layout warnings and font
substitution warnings. An overfull line may extend beyond its intended margin;
inspect the affected PDF page. Font substitutions should be reviewed against
the writing guidelines: the current text font is Times-like, not Times New Roman.
Chapter-only builds can also report missing PDF destinations for citations or
other chapters that are not included in that preview. The displayed citation
numbers and cross-reference text come from the full-document build, but links
to absent destinations cannot work in the standalone PDF.

The message `Wrote ...` at the end identifies the resulting PDF. If a task
fails, read its final error message rather than assuming an earlier warning
caused the failure.

---

## 3. Project Architecture & Modular Layout

All content is split into dedicated files so multiple team members can write concurrently without file locks or merge conflicts:

```text
Thesis Paper/
├── main.tex                # Master document and chapter selection
├── preamble.tex            # Shared packages and formatting
├── scripts/build.py        # Full and standalone preview builds
├── main.pdf                # Compiled proposal output (generated locally)
├── references.bib          # IEEE BibTeX database for citations
├── .gitignore              # Ignores build artifacts (*.aux, *.bbl, etc.)
├── .vscode/
│   ├── settings.json       # LaTeX Workshop settings
│   ├── tasks.json          # Full and preview build tasks
│   └── extensions.json     # Recommended extension
├── frontmatter/
│   ├── titlepage.tex       # Official ADNU ECE/CpE title page layout
│   └── abstract.tex        # Single-spaced abstract (100-200 words) + 5 keywords
├── chapters/
│   ├── ch1_intro.tex       # Ch 1: Introduction (Background, Problem, Significance, Objectives, Scope)
│   ├── ch2_lit_review.tex  # Ch 2: Literature Review (Related Studies, Theory, Synthesis)
│   ├── ch3_methodology.tex # Ch 3: Methodology (Model, Flowchart, Setup, Math, Cost, Evaluation)
│   ├── ch4_conclusion.tex  # Ch 4: Conclusion (synthesizes findings against objectives)
│   └── ch5_recommendation.tex # Ch 5: Recommendation (actionable future work)
├── appendices/
│   └── appendix_a.tex      # Appendix A: Project Gantt Chart and Timetable
└── figures/                # Assets folder for diagrams, flowcharts, and plots (.png, .pdf)
```

---

## 4. Daily Editing & Collaboration Workflow

### A. Compiling & Viewing the PDF
1. Open the project folder in VS Code and edit the appropriate `chapters/*.tex` file.
2. Save your changes with `Ctrl+S`.
3. Choose **Terminal → Run Task** and select the full thesis, chapter, or references task.
4. Open the resulting PDF in VS Code to inspect it. Use the full PDF for final review:
   standalone previews do not contain the other chapters.
5. Ask your AI assistant to explain unfamiliar LaTeX, then review its changes and
   citations against your source. Do not accept substantive changes without review.

### B. The "One-Sentence-Per-Line" Rule (Critical for Git)
To prevent Git merge conflicts across team members:
- **Write each sentence on its own separate line.** End each sentence with an `Enter` / newline.
- $\LaTeX$ automatically treats single line breaks as normal spaces in paragraphs, so document output is completely unchanged.
- **Why?** Git compares files line-by-line. If an entire paragraph is on one single line and two people edit different sentences, Git flags a collision. With one sentence per line, Git merges edits cleanly.

### Headings and Internal Labels
Use a heading command to create a visible, automatically numbered heading:
```latex
\section{Statement of the Problem}
\label{sec:statement_of_problem}
```
The section title appears in the PDF; the label is an internal identifier and
does not appear there. Refer to it elsewhere with
`Section~\ref{sec:statement_of_problem}`. After rebuilding, the reference uses
the current section number, even if sections have moved. Place a unique label
immediately after the heading; use `\subsection` and `\subsubsection` for
lower-level headings. The `~` keeps “Section” and its number together.

The same idea applies to figures and equations: give each a unique label and
refer to the label instead of typing a number. Rebuild after edits so references
and numbering update.

### C. In-Text Citations and the Bibliography
The proposal uses IEEE citations via `cite` and the `IEEEtran` bibliography style.
The source details live in `references.bib`; the numbered bibliography is
generated at the end of `main.pdf`. To inspect it separately, run
**Thesis: Build references** and open `build/previews/references.pdf`.

Each BibTeX entry has a unique citation key. For example, `ref1` in the current
database identifies Republic Act No. 9184. In a chapter, write:
```latex
... government contracts \cite{ref1}.
```
The PDF shows a numbered citation such as `[1]`, not the key. A key identifies
the source and does not have to match the number displayed. Choose a key by
**source identity**, not by the number you expect, and do not type citation
numbers manually.

To add a source, add an entry to `references.bib` using a new, unique key, then
cite that key in the relevant chapter. For example, this fictional journal
article demonstrates the syntax:
```bibtex
@article{cruz2025,
  author  = {Cruz, Maria and Santos, Juan},
  title   = {Document Processing for Public Procurement},
  journal = {Journal of Example Research},
  year    = {2025},
  volume  = {12},
  number  = {2},
  pages   = {45--60},
  doi     = {10.1234/example}
}
```
Then write `\cite{cruz2025}` where the claim needs that source. BibTeX formats
the entry in the generated bibliography; verify the details against the real
publication. The `and` between authors and `--` between page numbers are
BibTeX/LaTeX syntax.

The `@` entry type tells BibTeX what kind of source it is:
- `@article`: journal or magazine article.
- `@book`: book.
- `@inproceedings`: paper in conference proceedings.
- `@misc`: general-purpose entry for a source that does not fit neatly elsewhere.

Use the appropriate type and separate fields when possible. Some existing
`@misc` entries place already-written reference details in a `note` field.
Do not silently rewrite existing references: retain their source identity and
check their details. An AI assistant can help identify a type and draft an entry
from a DOI, URL, or title, but its output must be checked against the source.

The order of entries in `references.bib` does not set their PDF numbering:
cited sources are numbered by first appearance in the manuscript. Existing
uncited source entries are also retained by `main.tex` and appear afterward.
Rebuild after citation changes. The departmental guidelines show APA examples;
the project currently retains IEEE pending the later citation-style decision.

### D. Adding Tables & Figures (ADNU ECE/CpE Standards)
- **Tables (Captions on TOP, 1.5pt outer rules, 1.0pt inner rules, single-spaced):**
  ```latex
  \begin{table}[htbp]
  \centering
  \caption{Descriptive Title of Table}
  \label{tab:my_table}
  \begin{singlespace}
  \begin{tabular}{lcc}
  \toprule[1.5pt]
  \textbf{Parameter} & \textbf{Value} & \textbf{Unit} \\
  \midrule[1.0pt]
  Sample & 100 & ms \\
  \bottomrule[1.5pt]
  \end{tabular}
  \end{singlespace}
  \end{table}
  ```
- **Figures (Captions on BOTTOM with Source):**
  ```latex
  \begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/sample.png}
  \caption{System Architecture Flowchart}
  \label{fig:system_arch}
  \end{figure}
  \noindent\small Source: Author, Year
  ```
  Store the image file in `figures/` and use its actual filename in
  `\includegraphics`. The width is relative to the text area; the image's aspect
  ratio is preserved when only the width is specified. `\caption` produces the
  visible caption and number, while `\label` supplies the internal key.
  Refer to the figure with `Figure~\ref{fig:system_arch}`. LaTeX may move a
  figure to a suitable location; inspect the rendered PDF after building.
  Include a source attribution where appropriate.

### E. Equations and Cross-References
Use an equation environment for a numbered display and refer to its label rather
than typing a number. LaTeX updates the number when equations move.
```latex
\begin{equation}
\label{eq:example}
E = mc^2
\end{equation}
See Equation~\eqref{eq:example}.
```
Keep labels unique and use the existing source's notation and citation keys.
`\frac{N}{T}` writes a fraction. For short mathematical notation within a
sentence, use dollar signs: `The total time is $T$ seconds.` Numbered equations
use `\eqref{...}` to display the number in parentheses; figure and section
references use `\ref{...}`.

---

## 5. Git Collaboration Rules

1. **Confirm the branch and pull its latest changes before editing:**
   ```bash
   git branch --show-current
   git pull --ff-only
   ```
2. **Work on your assigned chapter:** coordinate with your partner to avoid
   editing the same text at the same time.
3. **Review, stage, and commit your intended files:**
   ```bash
   git status
   git add chapters/ch1_intro.tex
   git commit -m "Update Chapter 1"
   git push -u origin HEAD
   ```
   Replace the filename and commit message with the files and work you intend
   to share. The push command targets the currently checked-out branch.
