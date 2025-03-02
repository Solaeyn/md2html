# 📝 Markdown to HTML Converter (CLI)

<div align="center">

![Markdown to HTML](https://img.shields.io/badge/Markdown-HTML-orange)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**A powerful, feature-rich CLI tool that transforms your Markdown files into beautiful HTML documents.**

</div>

## ✨ Features

- **Multiple themes** - Choose from GitHub, Dark, Elegant, and Minimal styles
- **Directory processing** - Convert individual files or entire directories
- **Recursive mode** - Process nested folders with a single command
- **Syntax highlighting** - Automatically highlight code blocks
- **Table of Contents** - Generate navigable TOCs for your documents
- **Standalone mode** - Create self-contained HTML files with embedded CSS
- **Smart title detection** - Automatically uses your H1 heading as the document title
- **Custom styling** - Easy to add your own themes

## 🚀 Installation

### Requirements
- Python 3.6 or higher

### Install from Source

```bash
# Clone the repository
git clone https://github.com/Solaeyn/md2html.git
cd md2html

# Install the dependencies
pip install -r requirements.txt

# Optional: Make it available system-wide
pip install -e .
```

## 🔨 Usage

### Basic Usage

```bash
# Convert a single file (outputs to same directory with .html extension)
python md2html.py document.md

# Specify an output file
python md2html.py document.md -o output.html

# Convert with a specific theme
python md2html.py document.md --theme dark

# Create a standalone HTML file with CSS embedded
python md2html.py document.md --standalone
```

### Advanced Usage

```bash
# Convert a directory of markdown files
python md2html.py ./docs/

# Process directories recursively
python md2html.py ./docs/ -r

# Generate a table of contents
python md2html.py document.md --toc

# Enable syntax highlighting for code blocks
python md2html.py document.md --highlight

# Customize the document title
python md2html.py document.md -t "My Custom Title"
```

## 🎨 Available Themes

The converter comes with four beautiful themes:

- **GitHub** (default) - Clean and familiar GitHub style
- **Dark** - A sleek dark theme for easier reading at night
- **Elegant** - Typography-focused theme with serif fonts
- **Minimal** - A simple, distraction-free design

## 📋 Command Options

```
usage: md2html.py [-h] [-o OUTPUT] [-t TITLE] [--theme {github,elegant,dark,minimal}]
                  [-r] [--toc] [--highlight] [--standalone] [--version]
                  input

Convert Markdown files to beautifully styled HTML.

positional arguments:
  input                 Input markdown file or directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output HTML file or directory (default: same as input with .html extension)
  -t TITLE, --title TITLE
                        Document title (default: filename)
  --theme {github,elegant,dark,minimal}
                        HTML theme to use (default: github)
  -r, --recursive       Process directories recursively
  --toc                 Generate table of contents
  --highlight           Enable syntax highlighting
  --standalone          Include CSS in the HTML file
  --version             show program's version number and exit

Example: md2html input.md -o output.html --title "My Document" --theme github
```

## 🧩 Adding Custom Themes

1. Create a new CSS file in the `styles` directory
2. Name it something like `mytheme.css`
3. Add your styles (use the existing themes as a reference)
4. Modify the `md2html.py` file to include your theme in the choices list

## 📚 Examples

### Create a Blog Post
```bash
python md2html.py blog-post.md --theme elegant --highlight --standalone
```

### Generate Documentation Site
```bash
python md2html.py ./docs/ -r --theme github --toc
```

### Convert a Book
```bash
python md2html.py ./book/ -r --theme dark --toc -o ./published-book/
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Python-Markdown](https://python-markdown.github.io/) - Core markdown processing
- [Jinja2](https://jinja.palletsprojects.com/) - HTML templating
- [Pygments](https://pygments.org/) - Syntax highlighting

---

<div align="center">
  <p>Made with ❤️ for Markdown lovers</p>
  <p>Solaeyn</p>
</div>

