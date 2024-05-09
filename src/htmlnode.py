class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise Exception(NotImplementedError)
    
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
    def __init__(self, value,tag=None, props=None) -> None:
        self.value = value
        super().__init__(tag, self.value, None ,props)

    def to_html(self) -> None:
        if not self.value:
            raise Exception(ValueError)
        if self.props:
            if not self.tag:
                raise Exception(ValueError)
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        if self.tag:
            return f"<{self.tag}>{self.value}<{self.tag}>"
        return f"{self.value}"