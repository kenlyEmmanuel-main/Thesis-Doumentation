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

### C. In-Text Citations (IEEE Style)
The proposal uses `cite` and the `IEEEtran` bibliography style.
Use `\cite{key}` and add the corresponding source to `references.bib`:
```latex
Document layout analysis can use object detection \cite{ref29}.
```
Reference numbers are assigned by BibTeX in order of first citation.
The departmental writing guidelines show APA examples; confirm the required style with the adviser before changing the manuscript's citation style.
- To add a reference: Open `references.bib` and add your BibTeX entry.

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

---

## 5. Git Collaboration Rules

1. **Pull before you edit:**
   ```bash
   git pull origin main
   ```
2. **Work on your assigned chapter:**
   - Coordinate who edits which chapter file (`chapters/ch1_intro.tex` through `chapters/ch5_recommendation.tex`).
3. **Stage and commit your changes:**
   ```bash
   git add chapters/chX_yourchapter.tex references.bib
   git commit -m "Update Chapter X: added theoretical formulations and citations"
   git push origin main
   ```
