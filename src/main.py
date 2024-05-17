from textnode import TextNode
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import *


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
print(split_nodes_image([node]))

#raw_text = "This is **text** with an *italic* word **and** a [link](https://boot.dev) and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
#print("result is: ", text_to_textnodes(raw_text))