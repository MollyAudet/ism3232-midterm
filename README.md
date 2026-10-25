# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Molly Audet
- **Version:** 1.0
- **Date:** 10/25/2026

## What This Program Does
The following program helps Ridgeline Tool Rental's owner take a list of rentals and turn it into a consolidated report. For each rental received, it can calculate the customer's quote, apply any applicable discounts offered by the company, apply any fees, and show whether a deposit or pickup inspection is required. Finally, the report condenses all of that data into: the number of rentals, the total $ quoted, the average $ quote, the customer with the largest quote, and how many deposits and inspections are needed.

## Business Rules
The following six business rules are all implemented in business_rules.py and checked with pytest:
1. Rental Cost: Daily Rate * Number of days the equipment is rented for.
2. Customer Discount: The discount a customer receives pertains to the amount of days the equipment is rented for:
    - Less than 3 days = No discount
    - 3-6 days = 10% discount
    - 7 days or more = 20% discount
3. Contractor Discount: The additional benefit of being a contractor and renting with the company is always receiving at least a 10% discount, even on rentals less than 3 days.
4. Damage Waiver: $25 damage waiver is added when the discounted cost is under $150.
5. Deposit Requirement: A quote of $1,000 or more requires a deposit to rent out the equipment.
6. Pickup Inspections: A rental requires a pick-up inspection when it is used for 5 days or more and the quote is over $800.

## How to Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```bash
ruff format .
ruff check .
pytest -v
```
I wrote 26 tests in `tests/test_business_rules.py`.

## Files in This Repository
1. `business_rules.py`: contains the 8 functions built from the 6 business rules.
2. `main.py`: contains the rentals list and the code that prints the report.
3. `commands.md`: contains the record of how I built and checked the project.
4. `README.md`: contains the description of the project, how to run, tests, etc.
5. `requirements.txt`: contains the packages the project needs to run (pytest and ruff).
6. `.gitignore`: contains the files that git skips such as `.venv/` and `__pycache__/`.
7. `tests/__init__.py`: contains an empty file that makes `tests` a package.
8. `tests/test_business_rules.py`: contains the pytest tests for the eight functions.

## AI Use Statement
I did not use AI while taking the following exam.