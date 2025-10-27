| PRIORITY | ISSUE TYPE | TOOL | LOCATION | DESCRIPTION | FIX APPLIED |
|-----------|-------------|------|-----------|--------------|--------------|
| High | eval usage | Bandit | main()-line 59 | Security risk — allows arbitrary code execution | Removed eval; replaced with normal function calls or logging |
| High | Bare except: | Bandit / Pylint | removeItem() -line 19 | Swallows all exceptions, hides real bugs, and may mask critical errors | Used specific exception types (e.g., KeyError, ValueError) and proper logging |
| Medium | Mutable default argument | Pylint | addItem()-line 8 | Shared list across function calls can cause unpredictable behavior | Changed default to logs=None and initialize inside the function |
| Medium | No input validation | Pylint | addItem()-line 12 and getQty()-line 22 | Functions accepted wrong types (like int for item or str for qty), causing runtime errors | Added strict type checks and conversions; raised TypeError/ValueError when invalid |
| Low | File handling without with | Flake8 / Pylint | loadData()-line 25, saveData()-line 31 | Missing context manager can lead to file leaks and exceptions not handled properly | Used with open(...) as f: and handled FileNotFoundError & JSONDecodeError safely |
