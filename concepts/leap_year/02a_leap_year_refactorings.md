# 02a - Leap year refactorings

Previously we brough a leap year function under test.

```python
def leap_year(x):
    return (x % 4 == 0 and x % 100 != 0) or x % 400 == 0
```

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

It is time to refactor the function so that we can change it in the future. At this stage, we will **only** change the _structure_, **not** the _behaviour_.

## Rename `x` to `year` 

The first thing we will do is to rename the non-descriptive variable `x` to reflect what it stands for. In this case, a year.

```python
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
```

## Add type hints

We can also determine by the use of the [modulo](https://en.wikipedia.org/wiki/Modulo) operator `%` that the year is expected to be a number and by the fact that we are dealing with the concept of years that if further should be an integer. Also, we can see that the return value is a boolean expression.

Adding type hints could be helpful to convey this. 

```python
def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
```

## Predicate function name

The fact that this function has a boolean return value makes it a so called _predicate function_. Depending on what programming language you are using, there are conventions to denote that a function or method is a predicate. In Ruby for example, such method names can end with a trailing question mark. Python does not support this though, so instead it is a common practice to prepend `is_` to the name. Let us do that here.

```python
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
```

Of course, changing the name of the function will break any call sites (other places in the code base that calls this function) if we do not update those at the same time. Your development environment typically has support for doing this, but proceed carefully and **always** closely study any suggested changes before accepting them.

One of the most obvious places to update the name is of course the tests.

```python
def test_every_fourth_year_is_a_leap_year():
    assert is_leap_year(1980)

def test_every_hundreth_year_is_not_a_leap_year():
    assert not is_leap_year(1900)

def test_every_four_hundredth_year_is_a_leap_year():
    assert is_leap_year(2000)

def test_other_years_are_not_leap_years():
    assert not is_leap_year(1977)
```

Sometimes, we cannot change the call sites though. Perhaps we are working on a piece of code that is used outside of our code base and we would be changing the public API by renaming the function. This would break the concept of refactoring as we are changing the _behaviour_ and not only the _structure_.

In such cases, there is a _very_ simple way of ensuring that we do not break any call sites, nor the public API of our code.

```python
def is_leap_year(...):
    ...


leap_year = is_leap_year
```

## Split the logic

The single line logic might be clever, but quite cryptic and not very allowing for future change. Let us split the logic into separate clauses.

```python
def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
```

We still have a compound statement that we can break up. But, we need to rethink the order of how we check the year to do so.

```python
def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
```

How did we end up with the clauses in this order? Apart from reading the code and specification as well as reasoning about it, our tests act as a safety net to catch any invalid logical order.

## Name the mathematical operations

We repeatedly check if a given year is divisible by some value. We can make this clearer by extracting a helper function and name it accordingly.

```python
def is_leap_year(year: int) -> bool:
    if divisible_by(year, 400):
        return True
    elif divisible_by(year, 100):
        return False
    elif divisible_by(year, 4):
        return True
    else:
        return False


def divisible_by(dividend: int, divisor: int) -> bool:
    return dividend % divisor == 0
```

## Push details downwards

Can we better express that we are checking every fourth, hundredth, and fourhundreth year? Of course! We build upon the newly extracted function and introduce three more on top of it.

```python
def is_leap_year(year: int) -> bool:
    if every_four_hundredth(year):
        return True
    elif every_hundredth(year):
        return False
    elif every_fourth(year):
        return True
    else:
        return False


def every_four_hundredth(year: int) -> bool:
    return divisible_by(year, 400)


def every_hundredth(year: int) -> bool:
    return divisible_by(year, 100)


def every_fourth(year: int) -> bool:
    return divisible_by(year, 4)


def divisible_by(dividend: int, divisor: int) -> bool: 
    return dividend % divisor == 0
```

Notice that all the functions that we have introduced are indirectly tested through the tests we wrote for the original function. And despite the functions being predicate functions we did not name them as such. Why? No particular reason other than a personal preferance. 

## Overengineering: Is not a year more than just a number?

Python is an object-oriented language, and as such would it be farfetched to introduce a class for holding the logic and behaviour of a year?

```python
class Year:
    def __init__(self, year: int):
        self.year = year

    def divisible_by(self, divisor: int) -> bool:
        return self.year % divisor == 0
```

This allows us to refactor the function like this:

```python
def is_leap_year(year: int) -> bool:
    year = Year(year)
    if year.divisible_by(400):
        return True
    elif year.divisible_by(100):
        return False
    elif year.divisible_by(4):
        return True
    else:
        return False
```

And we can absolutely introduce additional methods to push the "magic" numbers 400, 100, and 4 downwards again.

```python
class Year:
    def __init__(self, year: int):
        self.year = year

    def every_four_hundredth(self) -> bool:
        return self.divisible_by(400)

    def every_hundredth(self) -> bool:
        return self.divisible_by(100)

    def every_fourth(self) -> bool:
        return self.divisible_by(4)

    def divisible_by(self, divisor: int) -> bool:
        return self.year % divisor == 0
```

```python
def is_leap_year(year: int) -> bool:
    year = Year(year)
    if year.every_fourhundredth():
        return True
    elif year.every_hundredth():
        return False
    elif year.every_fourth():
        return True
    else:
        return False
```

## Properties

While we are at it, let us turn those cases into properties so that we need not use parenthesis.

```python
class Year:
    def __init__(self, year: int):
        self.year = year

    @property
    def every_four_hundredth(self) -> bool:
        return self.divisible_by(400)

    @property
    def every_hundredth(self) -> bool:
        return self.divisible_by(100)

    @property
    def every_fourth(self) -> bool:
        return self.divisible_by(4)

    def divisible_by(self, divisor: int) -> bool:
        return self.year % divisor == 0
```

```python
def is_leap_year(year: int) -> bool:
    year = Year(year)
    if year.every_fourhundredth:
        return True
    elif year.every_hundredth:
        return False
    elif year.every_fourth:
        return True
    else:
        return False
```

## Reworking the names

A line such as `year.every_fourhundredth` grates a bit. How about we refer to that as a quadricentennial instead? We will even follow the predicate naming convention. The same goes with centennial instead of `every_hundredth` and quadrennial instead of `every_fourth`.

```python
    @property
    def is_quadricentennial(self) -> bool:
        return self.divisible_by(400)

    @property
    def is_centennial(self) -> bool:
        return self.divisible_by(100)

    @property
    def is_quadrennial(self) -> bool:
        return self.divisible_by(4)
```

The lesson to learn here is that in our natural languages we can find good, succinct names for concepts.


## Should not a year know if it is a leap year?

If we have introduced a `Year` class, why do we have to leap year logic existing outside of it? Granted, we still need to expose a function called `leap_year` or `is_leap_year`, but that function does not need to contain the logic. Rather, it can delegate it to the `Year` class.

```python
def is_leap_year(year: int) -> bool:
    return Year(year).is_leap_year()

leap_year = is_leap_year
```

```python
class Year:
    def __init__(self, year: int):
        self.year = year

    def is_leap_year(self) -> bool:
        if self.is_quadricentennial:
            return True
        elif self.is_centennial:
            return False
        elif self.is_quadrennial:
            return True
        else:
            return False        

    @property
    def is_quadricentennial(self) -> bool:
        return self.divisible_by(400)

    @property
    def is_centennial(self) -> bool:
        return self.divisible_by(100)

    @property
    def is_quadrennial(self) -> bool:
        return self.divisible_by(4)

    def divisible_by(self, divisor: int) -> bool:
        return self.year % divisor == 0
```

## Taking it too far

One pitfall we might have fallen into is taking our refactorings too far. By extracting a `Year` class _and_ moving the logic to determine whether a given year is a leap year or not into it, we have effectively locked ourselves into a design where a `Year` instance must know or be given knowledge of everything that goes into that determination. As we will see in a later step, there are more factors that come into play as the requirements change.
