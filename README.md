# Shining Carpet Pattern Generator

A Python project that generates and displays a tessellation of the iconic carpet pattern inspired by the movie *The Shining*. This project demonstrates text-based artistic output and is structured to include modular, reusable components with tests.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## About

The **Shining Carpet Pattern Generator** uses Python to create a repeated, text-based design inspired by the carpet seen in *The Shining*. The pattern can be customized by specifying horizontal (`x_repeat`) and vertical (`y_repeat`) repetitions.

---

## Features

- Generate a customizable, text-based carpet pattern.
- Modular design for easy extension and reuse.
- Fully tested with `unittest` framework.
- Lightweight and beginner-friendly.

---

## Installation

### Prerequisites

- Python 3.7 or higher.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shining-carpet.git
   cd shining-carpet
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements-dev.txt
   ```

---

## Usage

Run the project from the terminal:

```bash
python main.py
```

You can customize the pattern by modifying the `x_repeat` and `y_repeat` values in the `main.py` file.

---

## Project Structure

```plaintext
Shining_carpet/
├── shiningcarpet/
│   ├── __init__.py            # Makes the folder a package
│   ├── shiningcarpet.py       # Contains the ShiningCarpet class
├── tests/
│   ├── __init__.py            # Initializes the test package
│   ├── test_shiningcarpet.py  # Unit tests for ShiningCarpet class
├── main.py                    # Entry point to run the project
├── requirements-dev.txt       # Development dependencies
├── README.md                  # Project documentation
└── .flake8                    # Configuration for linting (optional)
```

---

## Testing

The project includes a suite of unit tests to ensure the correctness of the carpet generation and output logic. To run the tests:

```bash
python -m unittest discover -s tests
```

All tests are located in the `tests/` directory and use the `unittest` module.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

This project is inspired by the iconic carpet pattern from *The Shining* and is an example from *The Big Book of Small Python Projects* by Al Sweigart.

---

### Example Output

Below is an example of the generated carpet pattern:

```plaintext
_ \ \ \_/ __ _ \ \ \_/ __
 \ \ \___/ _  \ \ \___/ _
\ \ \_____/  \ \ \_____/ 
/ / /      \_/ / /      \_
 / / ______/   / / ______/ 
/ /_/      \  / /_/      \
```

Feel free to modify the pattern dimensions for your own experiments! 😊
