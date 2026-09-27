# Brain Games

[![hexlet-check](https://github.com/artem-mitasov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artem-mitasov/python-project-49/actions)

Brain Games is a set of five command-line games built with Python.

In each game, the player has to give three correct answers in a row. A wrong answer ends the game.

This project was created as part of the [Hexlet Python Developer course](https://ru.hexlet.io/programs/python).

## Requirements

- Python 3.14+
- uv

## Installation

Clone the repository:

```bash
git clone https://github.com/artem-mitasov/python-project-49.git
cd python-project-49
```

Build the package:

```bash
uv build
```

Install it as a command-line tool:

```bash
uv tool install dist/*.whl
```

After installation, the games can be launched directly from the terminal without `uv run`.

## Usage

Available commands:

```text
brain-games
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

### Brain Even

Determine whether a given number is even.

```bash
brain-even
```

[![asciicast](https://asciinema.org/a/yr3qX8uXLNXvOnDR.svg)](https://asciinema.org/a/yr3qX8uXLNXvOnDR)

### Brain Calc

Calculate the result of a randomly generated arithmetic expression.

```bash
brain-calc
```

[![asciicast](https://asciinema.org/a/lZq5eTJomPHSzgxh.svg)](https://asciinema.org/a/lZq5eTJomPHSzgxh)

### Brain GCD

Find the greatest common divisor of two numbers.

```bash
brain-gcd
```

[![asciicast](https://asciinema.org/a/X1EP7dvlAR9TIZrC.svg)](https://asciinema.org/a/X1EP7dvlAR9TIZrC)

### Brain Progression

Find the missing number in an arithmetic progression.

```bash
brain-progression
```

[![asciicast](https://asciinema.org/a/iFJkKIBq4qXiIo9t.svg)](https://asciinema.org/a/iFJkKIBq4qXiIo9t)

### Brain Prime

Determine whether a given number is prime.

```bash
brain-prime
```

[![asciicast](https://asciinema.org/a/H4HicPKSB8Hj6NOt.svg)](https://asciinema.org/a/H4HicPKSB8Hj6NOt)