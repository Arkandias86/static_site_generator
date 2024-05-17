from textnode import TextNode
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import *
from markdown_blocks import *


txtNode = TextNode("This is a text node", "link", "https://www.boot.dev")



htmlNode1 = HtmlNode(tag="p",value="Hello you!")
htmlNode2 = HtmlNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HtmlNode(tag="h1", children=htmlNode2)

#leafNode = LeafNode(tag="h1",value="" , props={"color": "red"})


text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"

node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
#print(split_nodes_image([node]))

raw_text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

print(markdown_to_blocks(raw_text))