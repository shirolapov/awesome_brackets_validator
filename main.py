import re
import unittest


def remove_pairs_of_brackets(string):
    # Remove pair symbols is valid brackets record. exc: ( (), {}, [] )
    new_string = re.sub(r"(\(\)|\[\]|{\})", "", string)
    if string == new_string:
        return new_string
    else:
        return remove_pairs_of_brackets(new_string)


def brackets_check(string):
    # Firstly cleaning checking string from all except brackets
    clear_string = re.sub(r"[^()\[\]{\}]", "", string)
    # String with only brackets checking on valid
    clear_string = remove_pairs_of_brackets(clear_string)
    # Valid string must be empty!
    if clear_string == "":
        return 1
    return 0


class TestBracketsMethod(unittest.TestCase):
    def test_brackets_check(self):
        self.assertEqual(brackets_check("((n*3)+[B/G+2])"), 1)
        self.assertEqual(brackets_check("(((n*3)+[B/G+2])"), 0)
        self.assertEqual(brackets_check("[2*(3]+5)"), 0)
        self.assertEqual(brackets_check("3/5+7"), 1)
        self.assertEqual(brackets_check("6^(4+5)/[7*8]]"), 0)
        self.assertEqual(brackets_check("6^(4+5)/[7*8]"), 1)


if __name__ == "__main__":
    unittest.main()
