# AGENTS.md

## Project overview

Single-file Python terminal e-commerce app. No build system, no external dependencies, no tests, no CI.

## Commands

```bash
python3 ecom_main_script.py
```

Interactive terminal loop — sends EOF on `stdin` to exit (Ctrl+D) or kills the process.

## Constraints

- **Standard library only.** No pip packages, no `requirements.txt`.
- `AGENT.md` (singular) is gitignored — it contains the backlog tracker. Read it to know what work still needs to be done.

## Tutoring mode

This is a teaching project. Agents **must** follow `AGENT.md`'s tutoring guidelines:
- Do **not** give complete code solutions. Provide insights, identify problems, and suggest critical first steps.
- Act as a straightforward, brutally honest code instructor.

## Architecture

- `ecom_main_script.py` — the only source file. Entrypoint is `main()` at the bottom of the file.
- Data structures: `dict` for inventory, `list` for order queue, `set` for unique customers.
- No modules, no packages, no imports beyond stdlib.
