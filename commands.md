# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
```
pwd 
mkdir ism3232-midterm
cd ~/ism3232/ism3232-midterm
git init
touch businessrules.py / main.py / commands.md / README.md 
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip list
pip freeze > requirements.txt
cat requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
cat .gitignore
ls -la
mkdir -p tests
cd ~/ism3232/ism3232-midterm/tests
touch test_business_rules.py / __init__.py
cd ..
git remote add origin <https://github.com/MollyAudet/ism3232-midterm>
code . business_rules.py
```

## 2. The virtual environment
```
which python3
```
```
/home/mollycodes/ism3232/ism3232-midterm/.venv/bin/python3
```
The indication of the venv being contained within ism3232-midterm points to it being run from a virtual environment as oppoased to the system Python (this is essential to keeping all packages installed in the project within that venv, making it easy to replicate on a second device when downloaded.)

## 3. The project structure
```
tree -L 2
```
```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```
A folder that appears on my computer but not in Github is the pycache, this appears as a result of being auto-generated cache file with Python, and does not appear due to .gitignore telling git to skip it.

## 4. Every function and test
```
rg 'def '
```
```
business_rules.py
17:def calculate_rental_cost(daily_rate: float, days: int) -> float:
22:def get_rental_discount(days: int, contractor: bool = False) -> float:
32:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
42:def requires_deposit(quote: float) -> bool:
47:def needs_inspection(days: int, quote: float) -> bool:
52:def total_quoted(rentals: list) -> float:
62:def largest_rental(rentals: list) -> str:
76:def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:

tests/test_business_rules.py
13:def test_rental_cost_at_five_days():
17:def test_no_discount_at_two_days():
21:def test_discount_is_ten_percent_at_three_days():
25:def test_discount_is_ten_percent_at_six_days():
29:def test_discount_is_twenty_percent_at_seven_days():
33:def test_contractor_discount_at_two_days():
38:def test_contractor_discount_at_eight_days():
42:def test_five_day_rental_gets_ten_percent_discount():
46:def test_two_day_rental_with_waiver():
50:def test_no_waiver_at_exactly_150():
54:def test_waiver_at_149_99():
58:def test_contractor_quote_at_eight_days_with_discount():
62:def test_contractor_quote_at_two_days_with_waiver():
66:def test_deposit_required_at_1000():
70:def test_deposit_required_at_999_99():
74:def test_no_inspection_at_four_days():
78:def test_no_inspection_at_exactly_800():
82:def test_inspection_required_at_five_days_and_quote_over_800():
86:def test_total_of_two_rentals():
94:def test_total_rental_of_empty_list_is_0():
98:def test_largest_rental_quote_is_first_in_list():
106:def test_largest_rental_quote_is_the_last_in_list():
114:def test_largest_rental_tie_returns_first_in_list():
122:def test_no_return_on_empty_list():
126:def test_format_rental_line_no_flags():
133:def test_format_rental_line_both_flags_and_four_digit_quote():
```
business_rules.py defines 8 seperate functions, with a total of 26 tests defined in tests/test_business_rules.py.

## 5. Which files print
```
rg -l 'print'
```
```
main.py
```

Main.py only prints since it contains print statements as opposed to business_rules.py (or main.py does the printing, while business_rules.py has the functions)

## 6. The commit history
```
git --no-pager log --oneline
```
```
Completed the main.py section with rental lists and confirmed report output.
1f3b601 Commit 5: Created format_rental_line function and associated tests.
4a35db3 Commit 4: Completed total_quoted and largest_rental functions with associated tests.
6feb49e Commit 3:Completed the requires deposit and needs inspection functions with limit tests; trimmed one rental cost test.
a001b35 commit 2: Removed stray businessrules.py, completed rental cost, rental discount, and quote functions with tests
848d20d Commit 1: Read over context for the Ridgeline Tool Rental, completed Part 1 of the exam.
```

I have six commits at this point, making the completion of this the seventh commit and the README.md as the final eighth commit. 
