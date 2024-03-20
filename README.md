
# AsciiDoc to Docusaurus Markdown Converter

This tool automates the conversion of AsciiDoc (.adoc) documents to Markdown (.md) files formatted for Docusaurus, including handling inline CSS styles for MDX compatibility. It streamlines the process into a single command, making it easy to prepare your documentation for Docusaurus deployment.

-----

## Features

- Converts AsciiDoc files to XML using `asciidoctor`.
- Transforms XML to strict Markdown using `pandoc`.
- Splits Markdown files by title, organizing content into separate directories for Docusaurus.
- Updates inline CSS to JSX style objects, making styles compatible with MDX format.

## Prerequisites

- Python 3.6 or newer.
- `asciidoctor` command-line tool.
- `pandoc` command-line tool.

Ensure both `asciidoctor` and `pandoc` are installed and accessible from your command line.

## Installation

No installation is necessary for the script itself, but ensure all prerequisites are met. You can clone this repository or download the script directly into your project.

## Usage

1. Place your AsciiDoc (.adoc) file in a known directory.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the conversion script.
4. Run the script with the path to your AsciiDoc file and the desired output directory for the Markdown files:

```bash
python converter.py /path/to/your/index.adoc /path/to/output/directory
```

Replace `/path/to/your/index.adoc` with the actual path to your AsciiDoc file, and `/path/to/output/directory` with the path where you want the converted Markdown files to be saved.

## How It Works

- The script first converts the AsciiDoc file to XML, then from XML to Markdown.
- It then processes the Markdown file, creating a separate directory for each section based on level 1 titles. Each section is saved in an `index.md` file within its respective directory.
- Inline CSS styles in the Markdown files are converted to JSX compatible style objects for use with MDX in Docusaurus.

## Customization

If you need to adjust the conversion process (e.g., handling specific inline styles or directory naming conventions), you can modify the script's Python functions. Ensure you have a basic understanding of Python and regular expressions to make these changes effectively.

## Troubleshooting

- **Command not found**: Ensure `python`, `asciidoctor`, and `pandoc` are correctly installed and in your system's PATH.
- **Conversion errors**: Check the syntax and format of your AsciiDoc file. Ensure it's compatible with `asciidoctor` and `pandoc`'s expected input formats.

For more detailed error information, run the script in a verbose or debug mode if available, or add print statements to the script to output error details.

## Roadmap
The AsciiDoc to Docusaurus Converter project is committed to continuous improvement and feature development. Here's a glimpse into our planned enhancements:

- **Add Unit Tests**: Implement comprehensive unit testing to ensure reliability and stability of the conversion process. This will help in automatically verifying the functionality of the tool against a wide range of AsciiDoc content and configurations, ensuring that future changes do not break existing functionality.
- **Improve Inline CSS Conversion**: Enhance the logic for converting inline CSS to MDX-compatible style objects, including support for more complex styles.
- **Interactive CLI**: Develop an interactive command-line interface (CLI) to offer users guided conversion processes, including customization options for the output. 
- **Documentation and Examples**: Create comprehensive documentation and example projects showcasing how to use the converter tool effectively in various scenarios.
- **Integration with CI/CD Pipelines**: Provide guidelines and templates for integrating the conversion tool into CI/CD pipelines, facilitating automated documentation deployments

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to suggest changes or additions.


