# dsh-superagent playground

A hands-on playground for following a `dsh-superagent` agent run from the first
commit to the last check.

A tiny sandbox repository for smoke-testing the `dsh-superagent` research prototype.
Nothing here is production code.

## Layout

- `greet.py` — greeting helpers `greet(name)`, `shout(name)` and `farewell(name)`.
- `tests/test_greet.py` — unittest coverage for them.
- `TASKS.md` — a few small, self-contained chores to hand the agent.

## Functions and command line

`greet.py` provides three functions. `name` is trimmed, and an empty or
whitespace-only name falls back to `朋友`.

- `greet(name)` returns the greeting `你好，<name>！` — for example, `greet("鱼")`
  returns `你好，鱼！`.
- `shout(name)` returns the greeting in uppercase — for example, `shout("alice")`
  returns `你好，ALICE！`.
- `farewell(name)` returns the farewell `再见，<name>！` — for example,
  `farewell("鱼")` returns `再见，鱼！`.

From the command line, pass the name as the first argument:

```sh
python3 greet.py 鱼  # prints 你好，鱼！
```

Running it without a name prints the usage message `用法: python3 greet.py <名字>`
and exits with code 1:

```sh
python3 greet.py
```

The command line only prints the `greet()` greeting; `shout()` and `farewell()`
are available from Python code.

## Run the tests

```sh
python3 -m unittest discover -s tests -v
```
