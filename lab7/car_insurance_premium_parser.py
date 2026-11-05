import re
from datetime import date, datetime

MAX_CLAIM_DIGITS = 9      # claims up to 999,999,999; also avoids huge int() conversions
MAX_DRIVER_AGE = 120


def normalize_registration(plate):
    """
    Removes spaces, dashes and dots from a registration number and upper-cases it.
    Returns an empty string if plate is not a string (e.g. None or a number).
    """
    if not isinstance(plate, str):
        return ""
    plate = plate.strip().upper()
    for ch in [' ', '-', '.']:
        plate = plate.replace(ch, '')
    # Remove any other whitespace (tabs, newlines, non-breaking spaces).
    return "".join(plate.split())


def total_claim_amount(text):
    """
    Adds up claim amounts separated by semicolons.
    Returns the total as an int, 0 for an empty input (no claims),
    or None if any amount is missing, negative, non-numeric or too large.
    """
    if not isinstance(text, str):
        return None
    text = text.strip()
    if text == "":
        return 0
    total = 0
    for amount in text.split(';'):
        amount = amount.strip()
        # ASCII digits only: rejects '', '-500', '12.5', '1e3', '²' and other
        # Unicode "digits" that int() cannot or should not convert.
        if not re.fullmatch(r"[0-9]{1,%d}" % MAX_CLAIM_DIGITS, amount):
            return None
        total += int(amount)
    return total


def driver_age(dob, current_year=2026):
    """
    Works out the driver's age in current_year from a DD/MM/YYYY date of birth.
    Returns None if dob is not a real DD/MM/YYYY date, is in the future,
    or gives an unrealistic age.
    """
    if not isinstance(dob, str) or not isinstance(current_year, int):
        return None
    dob = dob.strip()
    if not re.fullmatch(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", dob):
        return None
    try:
        born = datetime.strptime(dob, "%d/%m/%Y").date()   # rejects 31/02/2000, 00/13/1999
    except ValueError:
        return None
    if born > date.today() or born.year > current_year:
        return None
    age = current_year - born.year
    if not 0 <= age <= MAX_DRIVER_AGE:
        return None
    return age


def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    plate = normalize_registration(value)
    print("Normalized registration:", plate if plate else "Invalid registration number")

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    total = total_claim_amount(value)
    print("Total claimed:", total if total is not None
          else "Invalid input - use whole numbers separated by ;")

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    age = driver_age(value)
    print("Driver age in 2026:", age if age is not None
          else "Invalid date of birth - use DD/MM/YYYY")


if __name__ == "__main__":
    main()
