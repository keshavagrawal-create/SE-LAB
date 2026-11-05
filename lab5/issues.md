# Lab 5 — Issues Found and Fixed (`car_rental.py`)

Line numbers refer to the **original** file (`git show bb3a448:lab5/car_rental.py`).
High and medium severity findings are listed first.

## Security issues (Bandit)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Weak hash (B324) | Security — **High** | 48 | `hashlib.sha1` used to hash licence numbers; SHA-1 is broken for security use | Switched to `hashlib.sha256` |
| World-writable file (B103) | Security — **High** | 67 | `os.chmod(path, 0o777)` lets any user read/modify the booking receipt | Set permission to `0o600` (owner read/write only) |
| SQL injection (B608) | Security — **Medium** | 23, 26 | Queries built with `%` / string `+`; demo `"x' OR '1'='1"` dumped **every customer** | Parameterised queries with `?` placeholders |
| Use of `exec` (B102) | Security — **Medium** | 53 | Promo rule typed by staff is run with `exec()` — arbitrary code execution | Parse the rule with a strict regex (`amount = amount * <factor>`), accept only 0 < factor ≤ 1, else `ValueError` |
| Insecure temp file (B306) | Security — **Medium** | 63 | `tempfile.mktemp` is race-prone (file can be created by an attacker first) | `tempfile.mkstemp` + `os.fdopen` |
| Hard-coded password (B105, B107) | Security — Low | 70–71 | `"admin@rent"` hard-coded **and** used as the default, so `adminLogin("admin")` returned `True` | No default; password read from `CAR_RENTAL_ADMIN_PASSWORD` env var and compared with `hmac.compare_digest` |
| `assert` for validation (B101) | Security — Low | 30 | `assert` is stripped with `python -O`, so unregistered customers could rent | Raise `ValueError("Customer not registered")` |
| try/except/pass (B110) + bare except (W0702, E722) | Bug | 37–42 | Every error silently ignored; unknown car returned `None` with no message | Catch only `KeyError`, report the unknown plate |
| Insecure random (B311) | Security — Low | 45 | `random.randint` for booking codes is predictable | `secrets.randbelow` |

## Code-quality issues (Pylint)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Mutable default arg (W0102) | Bug | 16 | `features=[]` is shared between all cars | Default `None`, create a new list inside |
| Inconsistent returns (R1710) | Bug | 16, 36 | Functions return a value on some paths and nothing on others (`returnCar` gave `None` for ≤ 300 km) | Explicit `return None` / `return 0` |
| Unused import (W0611, F401) | Style | 2 | `json` imported but never used | Removed |
| Naming (C0103) | Style | 16–75 | camelCase function names | Renamed to snake_case (`add_car`, `rent_car`, …) |
| Missing docstrings (C0114, C0116) | Style | 1, all functions | No module/function documentation | Added docstrings |
| `open` without `with`/encoding (R1732, W1514) | Bug | 64 | File not closed on error; platform-dependent encoding | `with os.fdopen(fd, "w", encoding="utf-8")` |
| Simplifiable if / no-else-return (R1703, R1705) | Style | 57–60 | `if …: return True else: return False` | `return bool(re.match(...))` |
| `== True` comparison (C0121, E712) and dict iteration (C0206) | Style | 77–78 | Non-idiomatic loop | List comprehension over `fleet.items()` |
| `%` formatting (C0209) | Style | 23, 65 | Old-style string formatting | f-strings |
| Code runs on import | Style | 101 | `main()` called at module level | `if __name__ == "__main__":` guard |

## Style issues (Flake8 / PEP 8)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| E302 / E305 | Style | 16–82, 101 | 1 blank line between top-level functions instead of 2 | Added the missing blank lines |
| E501 | Style | 19, 23, 31, 33, 65, 88–90 | Lines longer than 79 characters | Wrapped lines, split the date parsing into two variables |

## Logic bugs found by running the program (not flagged by any tool)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Double booking | Bug | 29–34 | `rentCar` never set `available = False` — the Swift was rented twice | Mark the car unavailable; reject renting an unavailable car |
| Negative rental days | Bug | 31, 90 | End date before start date gave **Rs. −9000** | Reject bookings where `days <= 0` |
| Negative daily rate | Bug | 16, 85 | Nexon added with rate −500 | `add_car` raises `ValueError` for a negative rate |
| Unknown plate in `rentCar` | Bug | 32 | Raised a raw `KeyError` | Clear `ValueError("Unknown car: …")` |

## Result

| Tool | Before | After |
|------|--------|-------|
| Pylint | **4.94 / 10** | **10.00 / 10** |
| Bandit | 11 issues (2 High, 4 Medium, 5 Low) | **0 issues** |
| Flake8 | 25 issues | **0 issues** |
