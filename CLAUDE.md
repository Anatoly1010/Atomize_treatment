# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Working rules

- Plan in the main session, together with me. Hand grunt work (board searches, repetitive edits, boilerplate, log digging) to subagents on lesser models: Sonnet for searches, triage, and trivial mechanical work, and Opus for writing code. Keep decisions, architecture, and final review in the main session.
- Always look for the simplest solution first, and prefer it. The smallest change that solves the actual problem beats a bigger design, Extend existing patters before inventing new ones. No new dependencies or moving parts without a real reason.
- Show me a checklist while you work (use the todo list tool), keep current, so I can see what you are working on, what is done, and what is next.
- When you spawn a subagent, tell me at that moment: which model it runs on and what it is doing. Report what it came back with when it finishes.
- Never use Haiku.
- Comments: never multi-line. Omit the comment entirely when the code is obvious; otherwise one short line. Explain a fix in the commit message and the review/roadmap docs, not in the source. Docstrings are exempt (long explanatory docstrings are house style) but keep new ones tight.
- No over-explaining: Deliver the exact output requested. Do not narrate internal steps or show reasoning chains. Do not use programming jargon.
- Strict scope control: Stop when the requested task is complete. Do not expand, refactor unrequested areas, or suggest extra features.
- Use one commit per session.

## What this repo is

`Atomize_treatment` holds the optional data treatment tools of [Atomize](https://github.com/Anatoly1010/Atomize)
(sibling repo `../Atomize`): 1D and 2D data treatment, DEER analysis, the pulse sequence calculator,
excitation profiles and the spin-dynamics simulator, in `atomize/treatment/`. There is no
`atomize/__init__.py`, so the files join the core's `atomize` package, like a station's
(`../Atomize_stations`). Each tool is its own window and process, started by a command
(`pyproject.toml`) or by a station's main window with `python -m atomize.treatment.<tool>`.

The tools use only the core (`atomize.general_modules`, `atomize.math_modules`, `atomize.main`).
The math behind them (fitting, FFT, DEER, pulse excitation, spin dynamics) is in the core's
`math_modules/` and is changed there. Runtime files (the plot buffers from "Send to Data Treatment"
and the last-used folders) are in the running app's user config folder, see `atomize/treatment/paths.py`;
the main window side of "Send to Data Treatment" is in each station's `atomize/main/main.py`.

Check a change by opening the tool (`atomize-treatment`, …) with only the core installed and with a
station installed; `python -m atomize.treatment.sequence_calculator test` runs its self-test.
