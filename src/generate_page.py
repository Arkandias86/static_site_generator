

from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line
    raise Exception("header 1 is needed in the markdown")

def remove_first_directory(path):
    normalized_path = os.path.normpath(path)    
    path_parts = normalized_path.split(os.path.sep)
    
    if len(path_parts) > 1:
        path_parts = path_parts[1:]
    
    new_path = os.path.sep.join(path_parts)
    return new_path

def generate_page(from_path, template_path, dest_path):
    with open(from_path, "r") as markdown_file:
        markdown_content = markdown_file.read()
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
    parent_html_node = markdown_to_html_node(markdown_content)
    html_content = parent_html_node.to_html()
    header = extract_title(markdown_content)
    new_template = template_content.replace("{{ Title }}", header.replace("# ", ""))
    new_template = new_template.replace("{{ Content }}", html_content)
    with open(dest_path, "w") as file:
        file.write(new_template)
    


