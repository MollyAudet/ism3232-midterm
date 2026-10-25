from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def test_rental_cost_at_five_days():
    assert calculate_rental_cost(100, 5) == 500


def test_no_discount_at_two_days():
    assert get_rental_discount(2) == 0.00


def test_discount_is_ten_percent_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_discount_is_ten_percent_at_six_days():
    assert get_rental_discount(6) == 0.10


def test_discount_is_twenty_percent_at_seven_days():
    assert get_rental_discount(7) == 0.20


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


def test_deposit_required_at_1000():
    assert requires_deposit(1000.00) is True


def test_deposit_required_at_999_99():
    assert requires_deposit(999.99) is False


def test_no_inspection_at_four_days():
    assert needs_inspection(4, 900.00) is False


def test_no_inspection_at_exactly_800():
    assert needs_inspection(5, 800.00) is False


def test_inspection_required_at_five_days_and_quote_over_800():
    assert needs_inspection(5, 800.01) is True


def test_total_of_two_rentals():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    ]
    assert round(total_quoted(rentals), 2) == 278.00


def test_total_rental_of_empty_list_is_0():
    assert total_quoted([]) == 0.00


def test_largest_rental_quote_is_first_in_list():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    ]
    assert largest_rental(rentals) == "Alvarez"


def test_largest_rental_quote_is_the_last_in_list():
    rentals = [
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    ]
    assert largest_rental(rentals) == "Alvarez"


def test_largest_rental_tie_returns_first_in_list():
    rentals = [
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": True},
    ]
    assert largest_rental(rentals) == "Brennan"


def test_no_return_on_empty_list():
    assert largest_rental([]) == ""


def test_format_rental_line_no_flags():
    assert (
        format_rental_line("Alvarez", 145.00, False, False)
        == "Alvarez: $145.00 | deposit: no | inspection: no"
    )


def test_format_rental_line_both_flags_and_four_digit_quote():
    assert (
        format_rental_line("Eastman", 1344.00, True, True)
        == "Eastman: $1344.00 | deposit: yes | inspection: yes"
    )
