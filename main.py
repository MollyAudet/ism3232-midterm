# main.py

from business_rules import (
    calculate_quote,
    format_rental_line,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)

rentals = [
    {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    {"customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False},
    {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    {"customer": "Fujita", "daily_rate": 250.00, "days": 4, "contractor": False},
    {"customer": "Garza", "daily_rate": 95.00, "days": 5, "contractor": True},
    {"customer": "Hughes", "daily_rate": 200.00, "days": 7, "contractor": False},
]

print("Ridgeline Tool Rental - Rental Report")
count = 0
deposit_count = 0
inspection_count = 0
for rental in rentals:
    quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
    deposit = requires_deposit(quote)
    inspection = needs_inspection(rental["days"], quote)
    count += 1
    if deposit:
        deposit_count += 1
    if inspection:
        inspection_count += 1
    print(format_rental_line(rental["customer"], quote, deposit, inspection))

total = total_quoted(rentals)
print(f"Rentals: {count}")
print(f"Total quoted: ${total:.2f}")
print(f"Average quote: ${total / count:.2f}")
print(f"Largest quote: {largest_rental(rentals)}")
print(f"Deposits required: {deposit_count}")
print(f"Inspections required: {inspection_count}")
