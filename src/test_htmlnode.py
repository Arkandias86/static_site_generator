import unittest
from htmlnode import HtmlNode, LeafNode

htmlNode1 = HtmlNode(tag="p",value="Hello you!")
htmlNode2 = HtmlNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HtmlNode(tag="h1", children=htmlNode2)
leafNode1 = LeafNode(tag="h1",value="Hello World" , props={"color": "red"})
leafNode2 = LeafNode(tag="a",value="Awsome site" , props={"color": "red", "href": "www.boot.dev"})
leafNode3 = LeafNode(tag=None, value="Some text")
leafNode4 = LeafNode(tag="h1",value="")

correct_htmlNode1 = """\t~~~~~~~~~~~~~~~~~~~~~~~\ntag: p, value: Hello you!, props:None\n\t~~~~~~~~~~~~~~~~~~~~~~~\n\n"""
correct_propsNode2 = ''' href="http://www.kikoo.fr" color="orange"'''

class TestHtmlNode(unittest.TestCase):

    def test_no_props_no_child(self):
        return self.assertEqual(repr(htmlNode1), correct_htmlNode1)
    
    def test_props(self):
        return self.assertEqual(htmlNode2.props_to_html(), correct_propsNode2)
    
    def test_leaf_all(self):
        return self.assertEqual(leafNode1.to_html(), '''<h1 color="red">Hello World</h1>''')
    
    def test_leaf_all_href(self):
        return self.assertEqual(leafNode2.to_html(), '''<a color="red" href="www.boot.dev">Awsome site</a>''')
    
if __name__ == "__main__":
    unittest.main()