# 03a - The Excel bug

Last time we refactored our leap year function, probably to bits. Now it is time to add support for a few additional behaviours.

Since we will be changing _behaviour_ and not _structure_, we are no longer refactoring. We should also test-drive any new behaviour we are about to add.

## New requirement 1: the excel bug

Recall the rules for determining whether a year is a leap year or not? Excel missed that part back in the day so it concluded that 1900 is a leap year, despite it being a year divisible by a hundred. In order for us to support this, we are asked to introduce an optional flag to our function, denoting whether it should behave in an excel-compatible mode or not.

We start by adding a couple of test cases.

```python
def test_1900_with_excel_compatibility():
    assert is_leap_year(1900, excel_compatible=True)

def test_1900_without_excel_compatibility():
    assert not is_leap_year(1900, excel_compatible=False)
```

To eliminate an obviously incorrect implementation of just returning the flag, we also add a few more tests where it should make no difference on the result.

```python
def test_other_hundredth_year_with_excel_compatibility():
    assert not is_leap_year(1800, excel_compatible=True)

def test_other_hundredth_year_without_excel_compatibility():
    assert not is_leap_year(1800, excel_compatible=False)
```

For our implementation, let us assume that we stopped our refactorings before we introduced the `Year` class, but let us retain the better names.

This leads us to introduce the flag and implement it thusly:

```python
def is_leap_year(year: int, excel_compatible: bool = False) -> bool
    if is_quadricentennial(year):
        return True
    elif is_excel_compatible_1900(year, excel_compatible):
        return True
    elif is_centennial(year):
        return False
    elif is_quadrennial(year):
        return True
    else:
        return False


def is_excel_compatible_1900(year: int, excel_compatible: bool) -> bool:
    return excel_compatible and year == 1900
```

Now, that was admittedly a fairly small change to add support for a new behaviour. Had we instead worked with our unrefactored function, we would have had to implement it something like this.

```python
def leap_year(x, excel_compatible=False):
    return (x % 4 == 0 and x % 100 != 0) or x % 400 == 0 or (x == 1900 and excel_compatible)
```

## And then we refactor again!

> **NB:** This section is _not_ part of the course, but rather a deep-dive into a potential further, advanced refactoring. You have been warned.

Given that we no longer only care about the year, but also the excel compatibility, we might want to take another look at the concepts we are working with here. 

Looking at the structure of this function, we see that we are effectively testing a set of rules, one after another, until we find the first one that matches. At the very end we have our `else` as a catch-all.

What if we formulated the actual rules and then applied them one by one until we find one that matches?

```python
def is_leap_year(year: int, excel_compatible: bool=False) -> bool: 
    return any(map(lambda rule: rule(year, excel_compatible=excel_compatible), RULES))

def is_quadricentennial(year: int, **_) -> bool:
    return is_divisible_by(year, 400)

def is_centennial(year: int, **_) -> bool:
    return is_divisible_by(year, 100)

def is_quadrennial(year: int, **_) -> bool:
    return is_divisible_by(year, 4)

def is_divisible_by(dividend: int, divisor: int) -> bool: 
    return dividend % divisor == 0

def is_excel_compatible_centennial(year: int, excel_compatible: bool=False, **_) -> bool:
    return excel_compatible and is_centennial(year)

def is_non_centennial_quadrennial(year: int, **_) -> bool:
    return is_quadrennial(year) and not is_centennial(year)

RULES = [
    is_quadricentennial, 
    is_excel_compatible_centennial, 
    is_non_centennial_quadrennial
]
```

There are quite a few things to unpack here. Let us start with the `is_leap_year` function itself.

1. We use `any` to go through an iterable of values, looking for the first that is truthy, returning `True`. If none is found, it returns `False`.

2. The iterable in question is a lazily generated `map`, where a `callable` (here an inline `lambda`) is applied to each of the rules we have declared in our constant `RULES`. Each rule will be called with the `year` and any other options we may have; in our case `excel_compatible`.

3. `RULES` is a list of function pointers. A rule is a function that accepts a year and a variable amount of keyword arguments. Most of our rules only care for the year for now, but all must share the same API, the same contract, in that they also accept any number of keyword arguments.

4. We introduce and name new rules such as `is_excel_compatible_centennial` and `is_non_centennial_quadrennial` that in turn can be composed of other rules.

While this might seem quite excessive, we have effectively built a generic rules engine that with fairly minor tweaks could be applied to many other tasks than just our `is_leap_year` case. To truely make it generic, we should further break apart the coupling between the parameters `year` and `excel_compatible` on the one hand and the application of arguments to rules on the other hand. This will be left as an exercise to the reader.

## Resources

* A talk on [Creating and Using a Rules Engine](https://www.youtube.com/watch?v=Lsi1ZhmbNDc)
