# Reflection

1. Which issues were the easiest to fix, and which were the hardest?
-The easiest issues to fix were the basic code-quality problems flagged by Flake8 and Pylint.
-The hardest issues to fix were the security and logic problems identified by Bandit and Pylint

2. Did the static analysis tools report any false positives?
- Pylint flagged some variables and logging calls as “unused” or “redundant,” even though they were actually being used for debugging and record-keeping purposes.

3. How to integrate static analysis into development workflow?
- I would integrate Pylint, Bandit, and Flake8 into my workflow using pre-commit hooks and CI pipelines to automatically check code quality, security, and style before merging or deploying.

4. Tangible improvements after fixes?
- The code became more secure, readable, and maintainable with proper error handling, input validation, logging, and safe file operations replacing risky or unclear practices.

