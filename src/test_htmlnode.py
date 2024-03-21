import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_HTML(self):
        exception = NotImplementedError("Not implemented, you shouldn't be seeing this")
        node = HTMLNode("h1", "hello world", None, None)
        node2 = HTMLNode("p", "this is a test", None, "https://www.boot.dev/assignments/2ba3528c-8970-4579-aac8-980d1ddba2f0")
        self.assertRaises(NotImplementedError, node.to_HTML)
        self.assertRaises(NotImplementedError, node2.to_HTML)

    def test_props_to_HTML(self):
        node = HTMLNode("h1", "hello world", None, None)
        node2 = HTMLNode("a", "Click Me", None,{"href": "https://www.google.com"})
        for prop in node2.props:
            value2 = node2.props[prop]
            prop2 = prop
        self.assertEqual(node.props_to_HTML(), None)
        self.assertEqual(node2.props_to_HTML(), f" {prop}={value2}")
    
    def test__repr__(self):
        node = HTMLNode("h1", "hello world", None, None)
        node2 = HTMLNode("a", "Click Me", None, {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "HTMLNode: (h1, hello world, None, None)")
        self.assertEqual(node2.__repr__(), "HTMLNode: (a, Click Me, None, {'href': 'https://www.google.com'})")

    def test__leaf_to_HTML(self):
        node = LeafNode("h1", "hello world", None)
        node2 = LeafNode("a", "Click Me", {"href": "https://www.google.com"})
        node3 = LeafNode("h1", None, None)
        node4 = LeafNode(None, "hello world", None)
        self.assertEqual(node.to_HTML(), "<h1>hello world</h1>")
        self.assertEqual(node2.to_HTML(), "<a href=\"https://www.google.com\">Click Me</a>")
        self.assertRaises(ValueError, node3.to_HTML)
        self.assertEqual(node4.to_HTML(), "hello world")

    def test__parent_to_HTML(self):
        node = ParentNode(
            "h1",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_HTML(), "<h1><b>Bold text</b>Normal text<i>italic text</i>Normal text</h1>")
    
    def test__text_node_to_html_node(self):
        node_t = TextNode("This is text", "text")
        node_b = TextNode("This is bold", "bold")
        node_i = TextNode("This is italic", "italic")
        node_c = TextNode("This is code", "code")
        node_l = TextNode("This is a link", "link", "https://www.google.com")
        node_im = TextNode("This is an image", "image", "https://hips.hearstapps.com/fake-image.jpg")
        node_e = TextNode(None, None, None)
        self.assertEqual(node_t.text_node_to_html_node().__repr__(),  LeafNode(None, node_t.text).__repr__())
        self.assertEqual(node_b.text_node_to_html_node().__repr__(),  LeafNode("b", "This is bold").__repr__())
        self.assertEqual(node_i.text_node_to_html_node().__repr__(),  LeafNode("i", "This is italic").__repr__())
        self.assertEqual(node_c.text_node_to_html_node().__repr__(),  LeafNode("code", "This is code").__repr__())
        self.assertEqual(node_l.text_node_to_html_node().__repr__(),  LeafNode("a", "This is a link", {"href": "https://www.google.com"}).__repr__())
        self.assertEqual(node_im.text_node_to_html_node().__repr__(), LeafNode("img", "", {"src": "https://hips.hearstapps.com/fake-image.jpg", "alt": "This is an image"}).__repr__())
        self.assertRaises(TypeError, node_e.text_node_to_html_node)

        if __name__ == "__main__":
            unittest.main()