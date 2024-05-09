import unittest
from htmlnode import HtmlNode

htmlNode1 = HtmlNode(tag="p",value="Hello you!")
htmlNode2 = HtmlNode(tag="a", children=htmlNode1, props={"href": "http://www.kikoo.fr", "color": "orange"})
htmlNode3 = HtmlNode(tag="h1", children=htmlNode2)

correct_htmlNode1 = """\t~~~~~~~~~~~~~~~~~~~~~~~\ntag: p, value: Hello you!, props:None\n\t~~~~~~~~~~~~~~~~~~~~~~~\n\n"""
correct_propsNode2 = ''' href="http://www.kikoo.fr" color="orange"'''

class TestHtmlNode(unittest.TestCase):

    def test_no_props_no_child(self):
        return self.assertEqual(repr(htmlNode1), correct_htmlNode1)
    
    def test_props(self):
        return self.assertEqual(htmlNode2.props_to_html(), correct_propsNode2)
    
if __name__ == "__main__":
    unittest.main()