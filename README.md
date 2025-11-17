
# Learn Structures in Python

Small learning exercises for practicing basic Python data structures and simple scripts. These exercises were created while following Alura's course material and demonstrate small, focused examples (functions, loops, string handling, basic validation, etc.).

**Project**: A set of short Python examples grouped by exercise/topic.

## Project Structure

- `first_example/`: simple demonstration script (`sum.py`).
- `first_excercise/`: first exercise with `main.py`.
- `second_example/`: contains `main.py` and `counter.py` examples.
- `second_excercise/`: contains `validate_cpf.py` (CPF validation exercise).
- `third_excercise/`: contains `vogals_count.py` (vowel counting exercise).

## Requirements

- Python 3.8+ (3.10 or newer recommended)

## How to run

Each exercise is a small script you can run directly with Python. From the repository root run (using `bash` or a shell):

```bash
# Run a specific script file
python first_example/sum.py
python first_excercise/main.py
python second_example/main.py
python second_example/counter.py
python second_excercise/validate_cpf.py
python third_excercise/vogals_count.py

# Or run as a module (if you prefer):
python -m first_example.sum
```

Notes:
- Some scripts may prompt for input in the terminal. If a script accepts command-line args or expects interactive input, follow the prompts.
- If your system uses `python3` as the interpreter command, replace `python` with `python3`.

## Tips

- Use a virtual environment for experimentation: `python -m venv .venv && source .venv/bin/activate` (on Windows Git Bash use `source .venv/Scripts/activate`).
- Add tests or a small harness if you want to run many examples in sequence.

## Contributing

Open a pull request with improvements, additional exercises, or clearer explanations. Keep changes focused and add short descriptions for each new exercise.

## License

This repository contains learning exercises; no specific license is included. Add a `LICENSE` file if you want to specify reuse terms.

---
Happy learning! If you want, I can also:

- Add a `requirements.txt` or `pyproject.toml` if dependencies are needed.
- Add a short example output for each script.
