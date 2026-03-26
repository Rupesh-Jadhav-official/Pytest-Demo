# Pytest Implementation Overview

## Project Structure

```
tests/
├── __init__.py
├── test_Maths.py
├── test_String.py
└── test_dataframes.py
requirements.txt
report.html
```

## Test Files

### tests/test_Maths.py — Math unit tests
Functions-under-test and their tests live in the **same file** (no separate source module). Covers:
- `test_add_positive_numbers` / `test_add_negative_numbers` — basic addition via `assert`
- `test_divide_valid` — division with assertion
- `test_divide_by_zero` — exception handling using a manual `try/except` (rather than `pytest.raises`)

### tests/test_String.py — String unit tests
Same pattern — functions and tests co-located:
- `test_reverse_string` — tests string reversal
- `test_capitalize_string` — tests capitalization

### tests/test_dataframes.py — Pandas DataFrame tests
This file **does** import pytest directly and demonstrates:
- `@pytest.mark.skipif` — skips the test if `pandas` is not installed
- Multiple assertions within a single test function covering shape, columns, computed columns, and statistics

## Key Patterns Used

| Pattern | Where |
|---|---|
| Plain `assert` statements | All files |
| Manual `try/except` for exceptions | test_Maths.py lines 23–28 |
| `pytest.mark.skipif` conditional skip | test_dataframes.py line 8 |
| No fixtures or conftest.py | Project-wide |

## Dependencies (requirements.txt)
- `pytest` — test runner
- `pytest-html` — HTML report generation
- `pandas~=2.3.2` — used in the dataframe tests

## Running Tests

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests with HTML report
Run from the project root directory:
```bash
pytest tests --html=report.html --self-contained-html -v
```

### Open the HTML report
```bash
open report.html      # macOS
xdg-open report.html  # Linux
start report.html     # Windows
```

## Notes
- No fixtures, no `conftest.py`, and no parametrize are used
- Production code and tests are co-located in the same file
- This is a demo/learning project rather than a production-style layout
