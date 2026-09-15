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

### 3. Automated Compilation Recipe (`.vscode/settings.json`)
This repository comes preconfigured with `.vscode/settings.json`. It runs native Windows/cross-platform binaries without needing Perl or `latexmk`:
- **Recipe:** `pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`.
- **Auto-compile:** Triggers automatically whenever you save any `.tex` file (`Ctrl + S`).
- **Viewer:** Configured to open the compiled PDF directly inside an editor tab.

---

## 3. Project Architecture & Modular Layout

All content is split into dedicated files so multiple team members can write concurrently without file locks or merge conflicts:

```text
Thesis Paper/
├── main.tex                # Root master document (Preamble, ADNU margins, styles, includes)
├── main.pdf                # Compiled 17-page output document
├── references.bib          # APA BibTeX database for citations
├── .gitignore              # Ignores build artifacts (*.aux, *.bbl, etc.)
├── .vscode/
│   └── settings.json       # Native build recipes & IDE editor settings
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
1. Open any `.tex` file (or `main.tex`).
2. Make your edits and press `Ctrl + S`. The compilation pipeline runs in the background.
3. To view the PDF:
   - Click the **View LaTeX PDF** icon in the upper-right corner of the editor, or press `Ctrl + Alt + V` and choose **"View in Antigravity/VS Code Tab"**.
4. **SyncTeX Navigation (Jump between source & PDF):**
   - In `.tex`: `Ctrl + Left Click` on any line to jump directly to that position in the PDF viewer.
   - In PDF: `Ctrl + Left Click` on any text in the viewer to jump back to the exact `.tex` line.

### B. The "One-Sentence-Per-Line" Rule (Critical for Git)
To prevent Git merge conflicts across team members:
- **Write each sentence on its own separate line.** End each sentence with an `Enter` / newline.
- $\LaTeX$ automatically treats single line breaks as normal spaces in paragraphs, so document output is completely unchanged.
- **Why?** Git compares files line-by-line. If an entire paragraph is on one single line and two people edit different sentences, Git flags a collision. With one sentence per line, Git merges edits cleanly.

### C. In-Text Citations (APA Style)
We use `natbib` configured for APA author-date format:
- For narrative citations (e.g., *Vaswani et al. (2017) stated...*):
  ```latex
  \citet{vaswani2017attention} demonstrated that self-attention mechanisms...
  ```
- For parenthetical citations (e.g., *...as confirmed in previous studies (Goodfellow et al., 2016)*):
  ```latex
  \citep{goodfellow2016deep}
  ```
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
