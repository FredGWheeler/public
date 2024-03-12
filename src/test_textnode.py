import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a node", "italic", None)
        node2 = TextNode("this is a text node", "italic", None)
        self.assertEqual(node, node2)
    


    if __name__ == "__main__":
        unittest.main()