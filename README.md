## Learn Structures in Python

This repository gathers small exercises and examples used while studying how to properly structure Python projects. The goal is to go beyond writing scripts and practice building maintainable layouts with clear entry points, modules, and documentation.

### Objectives
- Experiment with different directory layouts (packages, modules, and tests)
- Practice separating responsibility across files
- Add lightweight tooling such as virtual environments, formatters, and linters
- Document learnings and decisions made while iterating on the structure

### Getting Started
1. Clone the repository.
2. Create and activate a virtual environment:
   - Windows (PowerShell): `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
   - Git Bash: `python -m venv .venv && source .venv/Scripts/activate`
3. Install tools or dependencies as you add them: `pip install -r requirements.txt` (create the file when needed).

### Suggested Project Layout
```
learn_structures_in_python/
├─ src/              # reusable application code
├─ tests/            # automated tests or exploratory notebooks
├─ docs/             # notes taken while experimenting
└─ README.md
```
Adapt this structure as the exercises evolve and capture the rationale in `docs/` so future you remembers the reasoning.

### Contributing Notes
This is primarily a personal learning space, but feel free to fork it or open issues with ideas on project organization tips, helpful links, or clarifying questions.