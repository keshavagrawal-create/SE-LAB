"""Car rental booking system.

Manages a fleet, customers, bookings, promos and receipts.
"""
import os
import re
import sqlite3
import hashlib
import hmac
import secrets
import tempfile
from datetime import datetime

# Global rental state
fleet = {}
bookings = []
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE customers (name TEXT, licence TEXT, phone TEXT)")


def add_car(plate, model="Unknown", daily_rate=0, features=None):
    """Add a car to the fleet and return its record (None if no plate)."""
    if not plate:
        return None
    if daily_rate < 0:
        raise ValueError("Daily rate cannot be negative")
    if features is None:
        features = []
    fleet[plate] = {"model": model, "rate": daily_rate,
                    "available": True, "features": features}
    return fleet[plate]


def register_customer(name, licence, phone):
    """Store a customer in the customers table."""
    conn.execute("INSERT INTO customers VALUES (?, ?, ?)",
                 (name, licence, phone))


def find_customer(name):
    """Return all customer rows matching the given name."""
    query = "SELECT * FROM customers WHERE name = ?"
    return conn.execute(query, (name,)).fetchall()


def rent_car(plate, customer, start, end):
    """Create a booking for a registered customer and return its cost."""
    if not find_customer(customer):
        raise ValueError("Customer not registered")
    if plate not in fleet:
        raise ValueError("Unknown car: " + plate)
    if not fleet[plate]["available"]:
        raise ValueError("Car " + plate + " is already rented")
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    days = (end_date - start_date).days
    if days <= 0:
        raise ValueError("End date must be after start date")
    cost = days * fleet[plate]["rate"]
    fleet[plate]["available"] = False
    bookings.append({"code": booking_code(), "plate": plate,
                     "customer": customer, "days": days, "cost": cost})
    return cost


def return_car(plate, km_driven):
    """Mark a car as returned and return the extra-kilometre charge."""
    try:
        fleet[plate]["available"] = True
    except KeyError:
        print("Unknown car:", plate)
        return None
    if km_driven > 300:
        return (km_driven - 300) * 5
    return 0


def booking_code():
    """Generate a random booking code such as BK-12345."""
    return "BK-" + str(10000 + secrets.randbelow(90000))


def licence_hash(licence):
    """Return a SHA-256 hash of a driving licence number."""
    return hashlib.sha256(licence.encode()).hexdigest()


def apply_promo(rule, amount):
    """Apply a promo rule like 'amount = amount * 0.9' to amount."""
    # rule is typed by the counter staff, e.g. "amount = amount * 0.9"
    # Only a multiplier between 0 and 1 is accepted instead of running exec().
    pattern = r"\s*amount\s*=\s*amount\s*\*\s*([0-9]*\.?[0-9]+)\s*"
    match = re.fullmatch(pattern, rule)
    if not match:
        raise ValueError("Unsupported promo rule: " + rule)
    factor = float(match.group(1))
    if not 0 < factor <= 1:
        raise ValueError("Promo multiplier must be between 0 and 1")
    return amount * factor


def is_valid_plate(plate):
    """Check that a number plate looks like KA01AB1234."""
    return bool(re.match(r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$", plate))


def write_receipt(booking):
    """Write a booking receipt to a private temp file and return its path."""
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(f"Booking {booking['code']}: {booking['plate']} for "
                f"{booking['days']} days = Rs.{booking['cost']}\n")
    os.chmod(path, 0o600)
    return path


def admin_login(user, password):
    """Check admin credentials against CAR_RENTAL_ADMIN_PASSWORD."""
    expected = os.environ.get("CAR_RENTAL_ADMIN_PASSWORD")
    if not expected:
        return False
    return user == "admin" and hmac.compare_digest(password, expected)


def available_cars():
    """Return the plates of all cars that are currently available."""
    return [plate for plate, car in fleet.items() if car["available"]]


def try_step(label, func, *args):
    """Run one demo step, printing its result or the error it raised."""
    try:
        print(label, func(*args))
    except ValueError as err:
        print(label, "rejected ->", err)


def main():
    """Run a short demo of the rental system."""
    add_car("KA01AB1234", "Swift", 1500)
    add_car("KA02CD5678", "Innova", 3000)
    try_step("Add Nexon:", add_car, "KA03EF9999", "Nexon", -500)
    register_customer("Ravi", "DL-0420110012345", "9845012345")
    register_customer("Meera", "DL-0420110099999", "9845099999")
    try_step("Rent Swift:", rent_car,
             "KA01AB1234", "Ravi", "2026-11-01", "2026-11-04")
    try_step("Rent Swift again:", rent_car,
             "KA01AB1234", "Ravi", "2026-11-02", "2026-11-03")
    try_step("Rent Innova:", rent_car,
             "KA02CD5678", "Ravi", "2026-11-10", "2026-11-07")
    print("Lookup injection:", find_customer("x' OR '1'='1"))
    print("Extra km charge:", return_car("KA01AB1234", 420))
    print("Return unknown car:", return_car("XX00XX0000", 50))
    print("Promo price:", apply_promo("amount = amount * 0.9", 4500))
    print("Plate valid?", is_valid_plate("KA01AB1234"))
    print("Licence hash:", licence_hash("DL-0420110012345"))
    print("Admin:", admin_login("admin", "guess"))
    print("Available:", available_cars())
    print("Receipt saved to:", write_receipt(bookings[0]))


if __name__ == "__main__":
    main()
