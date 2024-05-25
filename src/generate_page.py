

import shutil
from markdown_blocks import markdown_to_html_node
from copy_static import copy_files_recursive
import os

def generate_pages_recurse(nodepath, template_path, targetpath):
    print("In recursive generating")
    print("Path is: ", nodepath, "template path is: ", template_path, " target path is: ", targetpath)
    if not os.path.exists(nodepath):
        raise Exception("Not a valid path")
    content = [f for f in os.listdir(nodepath) if f != '.DS_Store']
    print("Content present in current path: ", content)
    if len(content) == 0:
        return None
    for node in content:
        npath = os.path.join(nodepath, node)
        print("current path is: ", npath)
        if not os.path.isfile(npath):
            newTargetDir = os.path.join(targetpath, node)
            print("targetDir is: ", newTargetDir)
            if not os.path.exists(newTargetDir):
                os.mkdir(newTargetDir)
                print("creating new dir: ", newTargetDir)
            print("recursing to npath=", npath, " and newTargetDir=", newTargetDir)
            generate_pages_recurse(npath, template_path, newTargetDir)
        else:
            generate_page(npath, template_path, targetpath)
            print("file: ", npath, " copied to targetPath: ", targetpath)
    return None

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
    print("In generate_page: from_path is: ", from_path, " template_path is: ", template_path, " dest_path is ", dest_path)
    with open(from_path, "r") as markdown_file:
        print("Opening markdownfile: ", from_path)
        markdown_content = markdown_file.read()
    with open(template_path, "r") as template_file:
        print("Opening template file from: ", template_path)
        template_content = template_file.read()
    print("Creating parent_html_node...")
    parent_html_node = markdown_to_html_node(markdown_content)
    print("Done!")
    print("Getting html content...")
    html_content = parent_html_node.to_html()
    print("Done!")
    print("title and content extration...")
    header = extract_title(markdown_content)
    new_template = template_content.replace("{{ Title }}", header.replace("# ", ""))
    new_template = new_template.replace("{{ Content }}", html_content)
    print("Done!")
    if dest_path != "":
        os.makedirs(dest_path, exist_ok=True)
        print("Destination dir is: ", dest_path)
    filename = os.path.basename(from_path).replace(".md", ".html")
    destination_filepath = os.path.join(dest_path, filename)
    with open(destination_filepath, "w") as file:
        print("writing file in destination dir")
        file.write(new_template)
        print("Done!")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    copy_files_recursive("static/", "public/")
    generate_pages_recurse(dir_path_content, template_path, dest_dir_path)



