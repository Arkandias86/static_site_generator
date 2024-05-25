from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import *
from markdown_blocks import *


txtNode = TextNode("This is a text node", "link", "https://www.boot.dev")



htmlNode1 = HTMLNode(tag="p",value="Hello you!")
htmlNode2 = HTMLNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HTMLNode(tag="h1", children=htmlNode2)

#leafNode = LeafNode(tag="h1",value="" , props={"color": "red"})


text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"

node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
#print(split_nodes_image([node]))

raw_text = """```
test
```"""

print(block_to_block_type(raw_text))