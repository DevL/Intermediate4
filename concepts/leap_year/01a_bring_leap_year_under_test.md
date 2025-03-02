# 01a - Bring leap year under test

This is a function implementing the logic for determining if a given year is a leap year according to the Gregorian calendar.

While the base rule is that a year divisible by four is a leap year, there are exceptions. Every hundred years is _not_ a leap year, _except_ for every four hundred years. This is to handle the fact that the mean tropical year is about 365.2422 days.

```python
def leap_year(x):
    return (x % 4 == 0 and x % 100 != 0) or x % 400 == 0
```

This code, while technically correct, has a number of problems that make it hard to add to. Which is exactly what we will do at a later step as the requirements on how to handle leap years change.

But first, we need to get it under test. Luckily, we have a fairly clear specification that we can use to formulate our tests.

* "Every 4 years is a leap year"
* "Every 100 years is not a leap year"
* "Every 400 years is a leap year"

We also need to test a year that falls in none of the three above categories, so we add a fourth test case.

* "Other years are not leap years"

We translate these cases into `pytest` code.

```python
def test_every_fourth_year_is_a_leap_year():
    assert leap_year(1980)

def test_every_hundreth_year_is_not_a_leap_year():
    assert not leap_year(1900)

def test_every_four_hundredth_year_is_a_leap_year():
    assert leap_year(2000)

def test_other_years_are_not_leap_years():
    assert not leap_year(1977)
```

Assuming that our tests pass with the existing code, we have now managed to bring it under test and can proceed to the next step; refactor it to make change easy.

## Resources

* Wikipedia's [article on leap years](https://en.wikipedia.org/wiki/Leap_year#Gregorian_calendar).
