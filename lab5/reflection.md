# Lab 5 — Reflection

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

The easiest were the Flake8 style issues and simple Pylint warnings: adding blank lines (E302), removing the unused `json` import, renaming functions to snake_case and adding docstrings. They are mechanical and do not change behaviour. The hardest was replacing `exec()` in `applyPromo`: removing it was easy, but the promo feature still had to work. I had to decide what a "safe" rule looks like (only `amount = amount * <factor>` with 0 < factor ≤ 1) and reject everything else. The hard-coded admin password was also tricky, because the fix is not just deleting a string — the password has to come from somewhere (an environment variable) and be compared safely with `hmac.compare_digest`.

**2. Did the static analysis tools report any false positives? If so, describe one example.**

Partly. Bandit's B311 (`random` is not cryptographically secure) is borderline for a booking code — it is an identifier, not a secret, so `random` would be acceptable in many apps. I still switched to `secrets` because a guessable booking code could let someone look up another customer's booking. Pylint's `invalid-name` and `missing-docstring` are not bugs either; they are conventions. On the other hand, the tools also **missed** real problems: the double booking, the negative cost of −9000 and the negative daily rate were only found by running the program and reading the output.

**3. How would you integrate static analysis tools into your actual software development workflow?**

Run Flake8 and Pylint automatically in the editor and as a **pre-commit hook**, so style problems never reach the repo. In **CI (GitHub Actions)**, run Pylint with a minimum score (for example `--fail-under=9.5`), Flake8, and Bandit on every pull request, and block merging if Bandit reports any Medium/High issue. Keep a shared config file (`.pylintrc`, `setup.cfg`) so the whole team uses the same rules, and use `# nosec` / `# pylint: disable` only with a comment explaining why.

**4. What tangible improvements did you observe in code quality, readability, or robustness after applying the fixes?**

- **Security:** the SQL-injection demo that previously returned *all* customers now returns `[]`; arbitrary code can no longer be run through the promo field; receipts are no longer world-writable; `adminLogin("admin")` no longer logs in with a default password.
- **Robustness:** errors are no longer silently swallowed; invalid input (negative rates, reversed dates, double booking, unknown cars) raises a clear `ValueError` instead of producing wrong numbers.
- **Readability:** consistent snake_case names, docstrings, f-strings and shorter lines make the file much easier to read and review.
- **Measurable:** Pylint went from **4.94 → 10.00**, Bandit from **11 → 0** issues and Flake8 from **25 → 0** issues, while the program still does its job.
