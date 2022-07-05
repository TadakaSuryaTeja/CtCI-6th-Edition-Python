# O(N)
import unittest


# O(1)
def string_rotation(s1: str, s2: str) -> bool:
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]
    
    # O(N)
    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
