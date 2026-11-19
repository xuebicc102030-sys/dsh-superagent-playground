import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("鱼"), "你好，鱼！")

    def test_empty_name_still_returns_text(self):
        self.assertEqual(greet(""), "你好，朋友！")


if __name__ == "__main__":
    unittest.main()
