# dsh-superagent playground

A tiny sandbox repository for smoke-testing the `dsh-superagent` research prototype.
Nothing here is production code.

## Layout

- `greet.py` — one function, `greet(name)`.
- `tests/test_greet.py` — unittest coverage for it.
- `TASKS.md` — a few small, self-contained chores to hand the agent.

## Run the tests

```sh
python3 -m unittest discover -s tests -v
```
