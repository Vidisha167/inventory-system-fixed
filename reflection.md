# Reflection

1. Which issues were the easiest to fix, and which were the hardest?
- Easiest: style issues (f-strings, using with open) because they are mechanical and low risk.
- Hardest: replacing bare except blocks and deciding whether to raise errors or ignore them — required thinking about intended behavior.

2. Did the static analysis tools report any false positives?
- Bandit sometimes flags patterns that are acceptable in controlled scripts (for example, certain uses of JSON loading), but in general its flags are helpful and motivated safer code.

3. How to integrate static analysis into development workflow?
- Add flake8/pylint/bandit to CI (GitHub Actions) to run on each PR. Use pre-commit hooks locally to catch problems before committing.

4. Tangible improvements after fixes?
- More robust input handling, improved logging, no dangerous eval calls, consistent JSON handling, and PEP8 improvements which aid readability and maintainability.
