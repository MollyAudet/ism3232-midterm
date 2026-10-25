# business_rules.py
# Author: Molly Audet


MID_TIER_DAYS = 3
HIGH_TIER_DAYS = 7
NO_DISCOUNT = 0.00
MID_TIER_DISCOUNT = 0.10
HIGH_TIER_DISCOUNT = 0.20
WAIVER_DAMAGE_FEE = 25.00
WAIVER_COST_LIMIT = 150.00
QUOTE_DEPOSIT_LIMIT = 1000.00
INSPECTION_DAYS_LIMIT = 5
INSPECTION_QUOTE_LIMIT = 800.00


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return total rental cost before any discounts or fees."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if days >= HIGH_TIER_DAYS:
        return HIGH_TIER_DISCOUNT
    elif contractor or days >= MID_TIER_DAYS:
        return MID_TIER_DISCOUNT
    else:
        return NO_DISCOUNT


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the quote for one rental: the discounted cost and the damage fee if applicable."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted_cost = cost * (1 - discount)
    if discounted_cost < WAIVER_COST_LIMIT:
        return discounted_cost + WAIVER_DAMAGE_FEE
    return discounted_cost


def requires_deposit(quote: float) -> bool:
    """Return True if the quote requires a deposit of $1,000 or more."""
    return quote >= QUOTE_DEPOSIT_LIMIT


def needs_inspection(days: int, quote: float) -> bool:
    """Return True when the rental needs a pickup inspection."""
    return days >= INSPECTION_DAYS_LIMIT and quote > INSPECTION_QUOTE_LIMIT


def total_quoted(rentals: list) -> float:
    """Return the total sum of the rentals for every rental in the list."""
    total = 0.00
    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
    return total


def largest_rental(rentals: list) -> str:
    """Return the customer with the largest rental quote, or "" for an empty list."""
    largest_customer = ""
    largest = 0.00
    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        if quote > largest:
            largest = quote
            largest_customer = rental["customer"]
    return largest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Return one line of the report."""
    deposit_text = "no"
    if deposit:
        deposit_text = "yes"
    inspection_text = "no"
    if inspection:
        inspection_text = "yes"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_text} | inspection: {inspection_text}"
