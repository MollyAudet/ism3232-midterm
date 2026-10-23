from business_rules import calculate_quote, calculate_rental_cost, get_rental_discount


def test_rental_cost_at_five_days():
    assert calculate_rental_cost(100, 5) == 500


def test_rental_cost_at_three_days():
    assert calculate_rental_cost(75, 3) == 225


def test_no_discount_at_two_days():
    assert get_rental_discount(2) == 0.00


def test_discount_is_ten_percent_at_six_days():
    assert get_rental_discount(6) == 0.10


def test_discount_is_twenty_percent_at_seven_days():
    assert get_rental_discount(7) == 0.20


def test_discount_is_ten_percent_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_contractor_discount_at_two_days():
    assert get_rental_discount(2) == 0.00
    assert get_rental_discount(2, contractor=True) == 0.10


def test_contractor_discount_at_eight_days():
    assert get_rental_discount(8, contractor=True) == 0.20


def test_five_day_rental_gets_ten_percent_discount():
    assert round(calculate_quote(100, 5), 2) == 450.0


def test_two_day_rental_with_waiver():
    assert round(calculate_quote(50, 2), 2) == 125.0


def test_no_waiver_at_exactly_150():
    assert round(calculate_quote(150, 1), 2) == 150.0


def test_waiver_at_149_99():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_contractor_quote_at_eight_days_with_discount():
    assert round(calculate_quote(100, 8, contractor=True), 2) == 640.0


def test_contractor_quote_at_two_days_with_waiver():
    assert round(calculate_quote(60, 2, contractor=True), 2) == 133.0
