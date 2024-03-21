class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_HTML(self):
        raise NotImplementedError("Not implemented, you shouldn't be seeing this")
    
    def props_to_HTML(self):
        if self.props == None:
            return None
        props = []
        for prop in self.props:
            value = self.props[prop]
            props = (f" {prop}={value}")
        return props
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_HTML(self):
        if self.value == None:
            raise ValueError("Leaf nodes require a value!")
        if self.tag == None:
            return self.value
        if self.tag == "a":
            for prop in self.props:
                value = self.props[prop]
                return f"<{self.tag} {prop}=\"{value}\">{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_HTML(self):
        if self.tag == None:
            return ValueError("Parent nodes must have a tag!")
        if self.children == None:
            return ValueError("Parent nodes must have children!")
        text = list(f"<{self.tag}>")
        for child in self.children:
            text.append(child.to_HTML())
        text.append(f"</{self.tag}>")
        text = "".join(text)
        return text
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.tag}, {self.children}, {self.props})"

    # def text_node_to_html_node(text_node):
    #     type = text_node.text_type
    #     if type == "text":
    #         return LeafNode(None, text_node.text)
    #     if type == "bold":
    #         return LeafNode("b", text_node.text)
    #     if type == "italic":
    #         return LeafNode("i", text_node.text)
    #     if type == "code":
    #         return LeafNode("code", text_node.text)
    #     if type == "link":
    #         return LeafNode("a", text_node.text, {"href": text_node.url})
    #     if type == "image":
    #         return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    #     else:
    #         raise TypeError("Text Node must be one of the following types:\ntext\nbold\nitalic\ncode\nlink\nimage")            

