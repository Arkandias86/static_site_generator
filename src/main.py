from textnode import TextNode
from htmlnode import HtmlNode

txtNode = TextNode("This is a text node", "bold", "https://www.boot.dev")
#print(repr(txtNode))

htmlNode1 = HtmlNode(tag="p",value="Hello you!")
htmlNode2 = HtmlNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HtmlNode(tag="h1", children=htmlNode2)

print(repr(htmlNode1))