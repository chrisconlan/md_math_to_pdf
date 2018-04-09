# LaTeX-Boosted Markdown to PDF

This is the last Markdown variant you will ever need. Features include:

+ LaTeX math, templates, and packages

+ YAML headers (Pandoc style)

+ Figure paths are relative to Markdown file, not working directory.

+ Can generate and save intermediate LaTeX.

+ Can call RMarkdown's Knitr to compute and interleave code in a handful of languages, including R and Python.

+ Uses Python 3's `subprocess.run()` for Bash safety.

## Usage

```
# As Python file
python3 main.py /path/to/markdown_doc.md

# As module
python3 -m math_md_to_pdf /path/to/markdown_doc.md

# Help output
python3 main.py --help
```

### Shebang and Symlink

Dump this in a script outside the project directory and symlink it to call from anywhere.

```
#!/usr/bin/python3 
import math_md_to_pdf
math_md_to_pdf.main()
```

## Dependencies

+ Python 3.5 or later for `subprocess.run()` and `print` functions.

+ Pandoc 1.12 for Markdown rendering. v1.12 required for YAML headers.

+ R with Knitr and RMarkdown if you want to execute code. This is controlled by an optional argument.

+ Currently uses `nohup` and `xdg-open` to open PDF's after rendering. This is also controlled by an optional argument.

## Background

RStudio supports most of these features by default through RMarkdown and Knitr. RStudio's default implementation of Pandoc was ultra-powerful, and I ended up using it to write two programming books.

I realized I needed a few more things from it:

+ I don't always want to evaluate the code. My second book had `{python, eval=False}` in every single chunk header because it used an isolated Python environment that couldn't be executed from Knitr.

+ I wanted filepaths to figures/pictures/images to be relative to the Markdown document, not the working directory from which the PDF is generated. This does wonders for portability and organization. (I made my technical reviewers download RStudio to edit my books, just to overcome this issue.)

+ I wanted to use other IDE's to write books and documentation. When writing, you really only use the top left window of RStudio.

+ I wanted to access my "knitting" utility from the command line.

+ I wanted to access my "knitting" utility from anywhere on my system. On my computer, a script sitting outside this directory shebang's `#!/usr/bin/python3`, runs `main.py`, and is symlinked to an easy-to-remember command.

+ I wanted to customize arguments passed to the core Pandoc call. RStudio provided a way of doing this via the GUI, but I found it lacking.

## Big Picture

I really liked the way that RStudio and Yihui Xie implemented Pandoc. It kickstarted my writing career in a huge way. I've finally gotten around to customizing it for my system.

## To-Do List

+ Add more cool arguments to Pandoc call. This is all that is required to make Pandoc produce the coolest Markdown flavor ever:

```
--to latex --from markdown+\
	autolink_bare_uris+\
	ascii_identifiers+\
	tex_math_single_backslash
```

+ Understand and add PDF templates. The ones in the `templates/latex` folder are taken from RStudio's installation directory, and work pretty well.

+ Add arguments to the command line utility, without overly duplicating Pandocs arguments.

## New Features

+ Can now use `--show_pdf_chrome` or `-c` to display the PDF in Google Chrome after rendering. This relies on `google-chrome` being callable from the command line.

+ For displaying the PDF with `xdg-open`, argument has been changed from `--show_pdf` to `--show_pdf_xdg`. I anticipate `--show_pdf_chrome` will be the more popular flag.


