from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

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