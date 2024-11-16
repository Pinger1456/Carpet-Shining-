"""Unit tests for the ShiningCarpet class. This module contains
a suite of tests for verifying the functionality
of the ShiningCarpet class, which generates a repeating text pattern
inspired by the carpet from the movie "The Shining"""

import unittest
from shiningcarpet import ShiningCarpet


class TestShiningCarpet(unittest.TestCase):
    """Unit test class for ShiningCarpet."""
    def test_generate_pattern(self):
        """Test that the pattern is generated correctly."""
        carpet = ShiningCarpet(x_repeat=2, y_repeat=1)
        expected_output = (
            "_ \\ \\ \\_/ __ _ \\ \\ \\_/ __\n"
            " \\ \\ \\___/ _  \\ \\ \\___/ _\n"
            "\\ \\ \\_____/  \\ \\ \\_____/ \n"
            "/ / /      \\_/ / /      \\_\n"
            " / / ______/   / / ______/ \n"
            "/ /_/      \\  / /_/      \\ "
        )
        self.assertEqual(carpet.generate_pattern(), expected_output)

    def test_empty_pattern(self):
        """Test that empty pattern is generated when repeats are zero."""
        carpet = ShiningCarpet(x_repeat=0, y_repeat=0)
        self.assertEqual(carpet.generate_pattern(), "")

    def test_negative_repeats(self):
        """Test that negative repeats raise an exception."""
        with self.assertRaises(ValueError):
            ShiningCarpet(x_repeat=-1, y_repeat=2)

    def test_pattern_line_count(self):
        """Test the number of lines in the pattern."""
        carpet = ShiningCarpet(x_repeat=1, y_repeat=2)
        output = carpet.generate_pattern()
        self.assertEqual(len(output.splitlines()), 12)  # 6 lines per repeat * 2 repeats

    def test_display(self):
        """Test that the display method works (mock stdout)."""
        carpet = ShiningCarpet(x_repeat=1, y_repeat=1)
        with self.assertLogs(level='INFO') as log:
            carpet.display()
        # Check the output contains part of the pattern
        self.assertIn("_ \\ \\ \\_/ __", log.output[0])


if __name__ == "__main__":
    unittest.main()
