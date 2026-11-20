import unittest

from greet import farewell, greet, shout


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("鱼"), "你好，鱼！")

    def test_empty_name_still_returns_text(self):
        self.assertEqual(greet(""), "你好，朋友！")

    def test_surrounding_spaces_are_trimmed(self):
        self.assertEqual(greet("  鱼  "), "你好，鱼！")

    def test_whitespace_only_name_still_returns_text(self):
        self.assertEqual(greet("   "), "你好，朋友！")

    def test_shout_uppercases_the_greeting(self):
        self.assertEqual(shout("alice"), "你好，ALICE！")

    def test_shout_of_chinese_name(self):
        self.assertEqual(shout("鱼"), "你好，鱼！")

    def test_farewell_by_name(self):
        self.assertEqual(farewell("鱼"), "再见，鱼！")

    def test_farewell_falls_back_for_empty_name(self):
        self.assertEqual(farewell(""), "再见，朋友！")
        self.assertEqual(farewell("   "), "再见，朋友！")


if __name__ == "__main__":
    unittest.main()
