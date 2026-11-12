"""Self-storage input processing helpers with defensive validation."""
import math


def _text(value, label):
    if not isinstance(value, str):
        raise ValueError(f"{label} must be text")
    return value.strip()


def parse_rental(text):
    """Parse ``unit:months``; reject malformed, non-finite, or negative months."""
    text = _text(text, "rental")
    if text.count(":") != 1:
        raise ValueError("rental must use unit:months format")
    unit, months_text = text.split(":")
    unit = unit.strip().title()
    if not unit or not months_text.strip():
        raise ValueError("unit and months are required")
    try:
        months = float(months_text.strip())
    except ValueError as exc:
        raise ValueError("months must be numeric") from exc
    if not math.isfinite(months) or months < 0:
        raise ValueError("months must be finite and non-negative")
    return unit, months


def duration_average(months_csv):
    """Return the floor of the mean of a non-empty CSV of non-negative integers."""
    months_csv = _text(months_csv, "months")
    parts = [part.strip() for part in months_csv.split(",")]
    if not parts or any(not part for part in parts):
        raise ValueError("provide one or more comma-separated month values")
    try:
        values = [int(part) for part in parts]
    except ValueError as exc:
        raise ValueError("months must be whole numbers") from exc
    if any(value < 0 for value in values):
        raise ValueError("months must be non-negative")
    return sum(values) // len(values)


def payable_rent(text):
    """Calculate rent plus 18% tax less discount, clamped at zero."""
    text = _text(text, "payment")
    if text.count("|") != 1:
        raise ValueError("payment must use rent|discount format")
    rent_text, discount_text = text.split("|")
    try:
        rent, discount = float(rent_text.strip()), float(discount_text.strip())
    except ValueError as exc:
        raise ValueError("rent and discount must be numeric") from exc
    if not math.isfinite(rent) or not math.isfinite(discount):
        raise ValueError("rent and discount must be finite")
    if rent < 0 or discount < 0:
        raise ValueError("rent and discount must be non-negative")
    total = rent * 1.18 - discount
    if not math.isfinite(total):
        raise ValueError("calculated rent is too large")
    return max(total, 0.0)


def main():
    tasks = (
        ("parse_rental", "Enter unit:months (e.g. medium:6): ", parse_rental,
         "Unit and Months:"),
        ("duration_average", "Enter rental months as CSV (e.g. 3,6,12): ", duration_average,
         "Average Duration:"),
        ("payable_rent", "Enter rent|discount (e.g. 2400|200): ", payable_rent,
         "Payable Rent:"),
    )
    for name, prompt, function, label in tasks:
        print(f"==== Running {name} ====")
        try:
            result = function(input(prompt))
        except ValueError as exc:
            print(f"Invalid input: {exc}")
        else:
            print(label, result)
        print()


if __name__ == "__main__":
    main()
