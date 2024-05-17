from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodeList = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            nodeList.append(node)
            continue
        if text_type == text_type_text:
            nodeList.append(node)
            continue
        splitted = node.text.split(delimiter)
        if len(splitted) < 2:
            nodeList.append(node)
            continue
        if len(splitted) % 2 == 0:
            raise Exception("no closing delimitter found")
        for i in range(len(splitted)):
            if i % 2 == 0:
                if len(splitted[i]) > 0:
                    nodeList.append(TextNode(splitted[i], "text"))
            else:
                if len(splitted[i]) > 0:
                    nodeList.append(TextNode(splitted[i], text_type))
    return nodeList

def extract_markdown_images(text):
    alt_text_URL = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alt_text_URL

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        images_markdowns = extract_markdown_images(node.text)
        if not images_markdowns:
            new_nodes.append(node)
            continue
        for image in images_markdowns:
            splitted = node.text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splitted) < 2:
                continue
            to_remove = f"{splitted[0]}![{image[0]}]({image[1]})"
            node.text = node.text.replace(to_remove, "", 1)
            if len(splitted[0]) > 0:
                new_nodes.append(TextNode(splitted[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
        if(node.text):
            new_nodes.append(TextNode(node.text, text_type_text))
    return new_nodes

def extract_markdown_links(text):
    anchor_text_URL = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return anchor_text_URL

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        links_markdowns = extract_markdown_links(node.text)
        if not links_markdowns:
            new_nodes.append(node)
            continue
        for link in links_markdowns:
            splitted = node.text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splitted) > 1:
                to_remove = f"{splitted[0]}[{link[0]}]({link[1]})"
                node.text = node.text.replace(to_remove, "", 1)
                if len(splitted[0]) > 0:
                    new_nodes.append(TextNode(splitted[0], text_type_text))
                new_nodes.append(TextNode(link[0], text_type_link, link[1]))
        if(node.text):
            new_nodes.append(TextNode(node.text, text_type_text))   
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes