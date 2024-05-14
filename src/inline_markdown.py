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
        splitted = node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise Exception("no closing delimitter found")
        for i in range(len(splitted)):
            if i % 2 == 0:
                nodeList.append(TextNode(splitted[i], "text"))
            else:
                nodeList.append(TextNode(splitted[i], text_type))
    return nodeList

def extract_markdown_images(text):
    alt_text_URL = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alt_text_URL

def extract_markdown_links(text):
    anchor_text_URL = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return anchor_text_URL

def split_nodes_image(old_nodes):
    node_text = old_nodes.text
    markdown_images_tuples = extract_markdown_images(node_text)
    images_nodes = []
    for tup in markdown_images_tuples:
        splitted = node_text.split(f"![{tup[0]}]({tup[1]})", 1)
        if splitted:
            images_nodes.append(TextNode(splitted[0], text_type_text))
            images_nodes.append(TextNode(tup[0], text_type_image, tup[1]))
            node_text = splitted[1] if len(splitted) > 1 else node_text
    return images_nodes

def split_nodes_link(old_nodes):
    node_text = old_nodes.text
    markdown_links_tuples = extract_markdown_links(node_text)
    links_nodes = []
    for tup in markdown_links_tuples:
        splitted = node_text.split(f"![{tup[0]}]({tup[1]})", 1)
        if splitted:
            links_nodes.append(TextNode(splitted[0], text_type_text))
            links_nodes.append(TextNode(tup[0], text_type_link, tup[1]))
            node_text = splitted[1] if len(splitted) > 1 else node_text
    return links_nodes
