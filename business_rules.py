# business_rules.py
# Author: [Molly Audet]

# Rules:
# 1. Rental cost = daily rate * number of days
# 2. Discount Rules:
# >3 Days: No Discount
# 3-6 Days: 10% Discount
# 7< Days: 20% Discount
# 3. Licensed Contractor: Always 10% Discount, even >3 Days
# 4. $25 damage waiver when the discounted cost is below $150
# 5. A quote of $1,000 or more requires a depost.
# 6. A rental needs a pickup inspection when it runs 5 days or more and its quote is over $800.

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


# uses rule 1
def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return total rental cost before any discounts or fees."""
    return daily_rate * days


# uses rule 2 and 3
def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if days >= HIGH_TIER_DAYS:
        return HIGH_TIER_DISCOUNT
    elif contractor or days >= MID_TIER_DAYS:
        return MID_TIER_DISCOUNT
    else:
        return NO_DISCOUNT


# uses rule 4 (but also the first two functions so rule 1-3 as well)
def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the quote for one rental: the discounted cost and the damage fee if applicable."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted_cost = cost * (1 - discount)
    if discounted_cost < WAIVER_COST_LIMIT:
        return discounted_cost + WAIVER_DAMAGE_FEE
    return discounted_cost


# uses rule 5
def requires_deposit(quote: float) -> bool:
    """Return True if the quote requires a deposit of $1,000 or more."""
    return quote >= QUOTE_DEPOSIT_LIMIT


# uses rule 6
def needs_inspection(days: int, quote: float) -> bool:
    """Return True when the rental needs a pickup inspection."""
    return days >= INSPECTION_DAYS_LIMIT and quote > INSPECTION_QUOTE_LIMIT


# uses sum of the quotes in every rental in the list; must use a for loop that calls calculate_quote
def total_quoted(rentals: list) -> float:
    """Return the total sum of the rentals for every rental in the list."""
    total = 0.00
    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
    return total

# returns the customer of the rental with the largest quote; two are tied? returns the one that comes first in the list. Empy list returns empty string.
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
