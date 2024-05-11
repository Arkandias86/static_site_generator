from htmlnode import LeafNode
class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: 'TextNode') -> bool:
        return value.text == self.text and value.text_type == self.text_type and value.url == self.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self) -> LeafNode:
        allowed_text_type = ["text", "bold", "italic", "code", "link", "image"]
        text_type = self.text_type

        if text_type not in allowed_text_type:
            raise Exception("Text type not handled by self_to_html_node")
        if text_type == "text":
            return LeafNode(None, self.text)
        if text_type == "bold":
            return LeafNode("b", self.text)
        if text_type == "italic":
            return LeafNode("i", self.text)
        if text_type == "code":
            return LeafNode("code", self.text)
        if text_type == "link":
            return LeafNode("a", self.text, {"href": self.url})
        if text_type == "image":
            return LeafNode("img", "", {"src": self.url, "alt": self.text})