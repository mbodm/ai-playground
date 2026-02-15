# ai-playground

Some playground repo for AI (like Codex or Claude).

## Hello World (Python)

`hello_world.py` now includes all three requested updates in one place:

1. **Function API** via `build_greeting(...)`.
2. **CLI option** support via `--name` and `--excited`.
3. **Bugfix** so empty/whitespace names fall back to `World`.

### Usage

```bash
python3 hello_world.py
python3 hello_world.py --name "Ada"
python3 hello_world.py --name "   " --excited
```
