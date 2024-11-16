"""Main script to run the Shining Carpet pattern generator."""

from shiningcarpet import ShiningCarpet

if __name__ == "__main__":
    # Default configuration for the carpet pattern
    carpet = ShiningCarpet(x_repeat=6, y_repeat=4)
    carpet.display()
