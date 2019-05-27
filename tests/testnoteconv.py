import unittest

import noteconv


class TestBaseNotes(unittest.TestCase):
    def test_case(self):
        for base_note in noteconv.base_notes:
            self.assertEqual(base_note, base_note.upper())


class TestToNote(unittest.TestCase):
    def test_middle_octave(self):
        self.assertEqual(noteconv.to_note('c'), noteconv.to_note('c', 5))

    def test_middle_c(self):
        self.assertEqual(noteconv.to_note('c'), 60)

    def test_middle_c_sharp(self):
        self.assertEqual(noteconv.to_note('c') + 1, noteconv.to_note('c#'))

    def test_a_440(self):
        self.assertEqual(noteconv.to_note('a', 5), 69)


if __name__ == '__main__':
    unittest.main()
