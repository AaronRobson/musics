import unittest

import noteconv

class TestToNote(unittest.TestCase):

    def test_middle_octave(self):
        self.assertEqual(noteconv.to_note('c'), noteconv.to_note('c', 5))

    def test_middle_c(self):
        self.assertEqual(noteconv.to_note('c'), 60)

    def test_a_440(self):
        self.assertEqual(noteconv.to_note('a', 5), 69)

if __name__ == '__main__':
    unittest.main()
