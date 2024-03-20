import subprocess
import os
import re


def convert_adoc_to_xml(adoc_file_path):
    """Converts AsciiDoc file to XML using the asciidoctor tool."""
    xml_file_path = f"{adoc_file_path.rsplit('.', 1)[0]}.xml"
    subprocess.run(['asciidoctor', '-b', 'docbook', adoc_file_path, '-o', xml_file_path], check=True)
    return xml_file_path


def convert_xml_to_md(xml_file_path):
    """Converts XML file to Markdown using the pandoc tool."""
    md_file_path = f"{xml_file_path.rsplit('.', 1)[0]}.md"
    subprocess.run(['pandoc', '-f', 'docbook', '-t', 'markdown_strict', xml_file_path, '-o', md_file_path], check=True)
    return md_file_path


def split_markdown_by_title(md_file_path, output_dir):
    """Splits the Markdown by title, creates directories within the output directory, and returns a dictionary of titles and their positions."""
    title_order = {}
    title_regex = re.compile(r'(^# .+?$)(.*?)(?=^# |\Z)', re.MULTILINE | re.DOTALL)

    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    matches = title_regex.findall(content)
    position = 1

    for match in matches:
        title_line, text = match
        title = title_line[2:].strip()
        safe_title = re.sub('[^a-zA-Z0-9\n\.]', '-', title).lower()
        directory_name = os.path.join(output_dir, safe_title)

        os.makedirs(directory_name, exist_ok=True)
        file_name = os.path.join(directory_name, 'index.md')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n{text.strip()}")

        title_order[safe_title] = position
        position += 1

        print(f"Directory and file '{file_name}' has been created.")
    return title_order


def update_md_for_docusaurus(output_dir='output', title_order=None):
    """Updates the Markdown files for Docusaurus by setting the sidebar position."""
    if title_order is None:
        title_order = {}

    style_attr_regex = re.compile(r'style="([^"]+)"')

    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file == 'index.md':
                md_file_path = os.path.join(root, file)
                directory_name = os.path.basename(root)
                position = title_order.get(directory_name, 1)

                with open(md_file_path, 'r', encoding='utf-8') as md_file:
                    # Read the entire content as a single string
                    content = md_file.read()

                # Convert style attributes to style objects, handling the conversion to a JSON-like syntax
                content = style_attr_regex.sub(lambda m: f"style={convert_css_to_object(m.group(1))}", content)

                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    lines = content.split('\n', 1)
                    title = lines[0].strip('# \n')
                    docusaurus_front_matter = f"---\nsidebar_position: {position}\ntitle: {title}\n---\n\n"
                    # Prepend the Docusaurus front matter to the rest of the content
                    md_file.write(docusaurus_front_matter + content)

                print(f"Updated {md_file_path} for Docusaurus.")


def kebab_to_camel_case(value):
    """Converts CSS property names from kebab-case to camelCase."""
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(value.split('-')))


def convert_css_to_object(css_string):
    """Converts a CSS string to a JS object string format for inline styles in MDX/JSX."""
    styles = [s.strip() for s in css_string.split(';') if s.strip()]
    obj_styles = []
    for style in styles:
        if ':' in style:
            prop, val = style.split(':', 1)
            prop = kebab_to_camel_case(prop.strip())
            val = val.strip().replace('"', '\\"')  # Escape double quotes
            obj_styles.append(f"{prop}: '{val}'")
    return '{{' + ', '.join(obj_styles) + '}}'


def run(adoc_index_path, output_dir):
    """Main conversion flow."""
    xml_file_path = convert_adoc_to_xml(adoc_index_path)
    md_file_path = convert_xml_to_md(xml_file_path)
    title_order = split_markdown_by_title(md_file_path, output_dir)
    update_md_for_docusaurus(output_dir, title_order)


# Example usage
adoc_index_path = '../.test/dev-practices/src/index.adoc'
output_dir = '../.test/output'
run(adoc_index_path, output_dir)
