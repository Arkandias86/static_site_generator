class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return None
        str_html = ""
        for key, value in self.props.items():
            str_html += " " + key + '="' + value + '"'
        return str_html
    
    def print_children(self, children, child_string="") -> str:
        if not children:
            return child_string
        child_string = self.print_children(children.children, child_string)
        str_props = ""
        if children.props:
            str_props = children.props_to_html()
        child_string += f"\t~~~~~~~~~~~~~~~~~~~~~~~\ntag: {children.tag}, value: {children.value}, props:{str_props if str_props else None}\n\t~~~~~~~~~~~~~~~~~~~~~~~\n\n" 
        return child_string
            
    def __repr__(self) -> str:
        children_list_string = self.print_children(self)
        return children_list_string
    
class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None ,props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Invalid HTML: no value")
        if self.props:
            if not self.tag:
                raise ValueError("Invalid HTML: no tag")
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"{self.value}"
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None) -> None:
        #if value:
        #    raise ValueError("Error in HTML, parent node can't have values")
        if not tag:
            raise ValueError("Error in HTML, parent node need tags")
        super().__init__(tag, None, children, props)
    
    def to_html_one(self) -> str:
        if not self.tag:
            return f"{self.value}"
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
        

    def recurse_print(self, html_string="") -> str:
        if not self.children:
            return f"{html_string} + {self.to_html_one()}"
        for child in self.children:
            if child.children:
                html_string += child.recurse_print(html_string)
            else:    
                html_string += child.to_html()
        return f"<{self.tag}>{html_string}</{self.tag}>"
        

    def to_html(self) -> str:
        return self.recurse_print()
    