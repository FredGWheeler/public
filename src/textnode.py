from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode):
        if (
            self.text == TextNode.text 
            and self.text_type == TextNode.text_type 
            and self.url == TextNode.url
        ):
            return True
        else:
            return False
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
    def text_node_to_html_node(text_node):
        type = text_node.text_type
        if type == "text":
            return LeafNode(None, text_node.text)
        if type == "bold":
            return LeafNode("b", text_node.text)
        if type == "italic":
            return LeafNode("i", text_node.text)
        if type == "code":
            return LeafNode("code", text_node.text)
        if type == "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if type == "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise TypeError("Text type not recognized, expected one of:  text, bold, italic, code, link, image")