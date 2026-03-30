# Pytest Demo — Project Overview

## Project Structure

```
Pytest Demo/
├── tests/
│   ├── __init__.py          ← makes tests/ a Python package
│   ├── test_Maths.py        ← unit tests for math functions
│   ├── test_String.py       ← unit tests for string functions
│   └── test_dataframes.py   ← tests with pandas + conditional skip
├── requirements.txt         ← project dependencies
├── report.html              ← generated HTML test report
└── pytest_overview.md       ← documentation
```

---

## What is pytest?

**pytest** is a Python testing framework used to write and run unit, integration, and functional tests. It is the industry standard for Python testing because:

- No boilerplate — no need to extend a class or use `self`
- Uses plain `assert` statements instead of special assertion methods
- Auto-discovers test files and functions by naming convention
- Has a rich plugin ecosystem (e.g., `pytest-html`)

---

## Interview Q&A — Core Concepts

---

### Q: How does pytest discover tests?

pytest uses **naming conventions** to auto-discover tests:
- Files must be named `test_*.py` or `*_test.py`
- Functions inside must start with `test_`
- Classes (optional) must start with `Test`

In this project, `tests/test_Maths.py`, `tests/test_String.py`, and `tests/test_dataframes.py` are all picked up automatically.

---

### Q: What is a unit test?

A unit test verifies a **single isolated piece of logic**. In `tests/test_Maths.py`:

```python
def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, f"Expected 5, got {result}"
```

- **Arrange** — define inputs (`2, 3`)
- **Act** — call the function (`add(2, 3)`)
- **Assert** — verify the output (`== 5`)

This is called the **AAA pattern** (Arrange-Act-Assert).

---

### Q: How do you test that a function raises an exception?

Two approaches are shown in this project:

**Manual try/except** (used in `tests/test_Maths.py`):
```python
def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected ValueError but no exception was raised"
    except ValueError:
        pass  # Expected behavior
```

**The pytest-idiomatic way** (not used here, but the preferred pattern):
```python
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

`pytest.raises` is cleaner and produces better failure messages. This project uses the manual approach — worth mentioning in an interview as something you would improve.

---

### Q: What is `pytest.mark.skipif`?

A **marker** that conditionally skips a test at runtime. In `tests/test_dataframes.py`:

```python
@pytest.mark.skipif(pd is None, reason="pandas is not installed")
def test_dataframe_operations():
    ...
```

- If `pandas` is not installed, `pd` will be `None` (see the `try/except ImportError` above it)
- The decorator tells pytest to skip this test with a descriptive reason
- This avoids `ImportError` crashes and makes the test suite **environment-aware**

---

### Q: What is `__init__.py` in the tests folder?

It marks the `tests/` directory as a **Python package**, allowing pytest to resolve imports correctly when test files reference each other or shared modules. Without it, relative imports between test files can fail.

---

### Q: What is `requirements.txt`?

A plain text file listing project dependencies:
```
pytest
pytest-html
pandas~=2.3.2
```

- `pytest` — the test runner
- `pytest-html` — plugin that generates an HTML test report
- `pandas~=2.3.2` — compatible with `2.3.x` (the `~=` is the "compatible release" specifier)

Install with:
```bash
pip install -r requirements.txt
```

---

### Q: How do you run tests and generate an HTML report?

```bash
pytest tests --html=report.html --self-contained-html -v
```

| Flag | What it does |
|---|---|
| `tests` | Run tests inside the `tests/` folder |
| `--html=report.html` | Generate HTML report via `pytest-html` plugin |
| `--self-contained-html` | Embed CSS/JS into a single HTML file |
| `-v` | Verbose output — shows each test name and pass/fail |

---

### Q: What patterns are demonstrated in this project?

| Pattern | File | Description |
|---|---|---|
| Plain `assert` | All files | Core pytest assertion mechanism |
| Custom failure message | `test_Maths.py` | `assert result == 5, f"Expected 5, got {result}"` |
| Manual exception testing | `test_Maths.py` | try/except pattern |
| Conditional skip | `test_dataframes.py` | `@pytest.mark.skipif` |
| Safe optional import | `test_dataframes.py` | `try: import pandas except ImportError: pd = None` |

---

### Q: What's missing that a production project would have?

This is explicitly a **demo/learning project**. Production projects would typically add:

| Missing | Purpose |
|---|---|
| `conftest.py` | Shared fixtures across test files |
| `@pytest.fixture` | Reusable setup/teardown (e.g., DB connection, temp files) |
| `@pytest.mark.parametrize` | Run one test with many input combinations |
| Separate `src/` and `tests/` | Production code lives outside the test folder |
| `pytest.raises` | Preferred over manual try/except |
| `pytest.ini` / `pyproject.toml` | Central pytest configuration |

---

### Q: What is a fixture?

Not used here, but fundamental to pytest. A **fixture** is a reusable setup function:

```python
@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({"Name": ["Alice"], "Age": [25]})

def test_something(sample_dataframe):
    assert len(sample_dataframe) == 1
```

pytest injects it by matching the parameter name. Fixtures support **scope** (`function`, `class`, `module`, `session`) to control how often they run.

---

## Summary

This project is a clean beginner-level demonstration of pytest's most fundamental capabilities:

- Auto-discovery by naming convention
- Plain `assert` statements with custom messages
- AAA pattern (Arrange-Act-Assert)
- Exception testing via try/except
- Conditional test skipping with `@pytest.mark.skipif`
- HTML report generation with `pytest-html`
