"""Shining Carpet Module.

Provides the ShiningCarpet class for generating the carpet pattern.
"""


class ShiningCarpet:
    """Class to generate and display the Shining Carpet pattern."""
    def __init__(self, x_repeat: int = 6, y_repeat: int = 4):
        """Initialize with horizontal and vertical repetition counts."""
        self.x_repeat = x_repeat
        self.y_repeat = y_repeat

    def generate_pattern(self) -> str:
        """Generate the carpet pattern as a string."""
        lines = []
        for _ in range(self.y_repeat):
            lines.append(r'_ \\ \\ \\_/ __' * self.x_repeat)
            lines.append(r' \\ \\ \\___/ _' * self.x_repeat)
            lines.append(r'\\ \\ \\_____/ ' * self.x_repeat)
            lines.append(r'/ / /      \\_' * self.x_repeat)
            lines.append(r' / / ______/ ' * self.x_repeat)
            lines.append(r'/ /_/      \\ ' * self.x_repeat)
        return "\n".join(lines)

    def display(self) -> None:
        """Print the generated carpet pattern."""
        print(self.generate_pattern())
