from textnode import TextNode
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import *


txtNode = TextNode("This is a text node", "link", "https://www.boot.dev")



htmlNode1 = HtmlNode(tag="p",value="Hello you!")
htmlNode2 = HtmlNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HtmlNode(tag="h1", children=htmlNode2)

#leafNode = LeafNode(tag="h1",value="" , props={"color": "red"})

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node = TextNode("This is text with a **bold block** word", "text_type_text")
new_nodes = split_nodes_delimiter([node], "**", "text_type_bold")

print(new_nodes)