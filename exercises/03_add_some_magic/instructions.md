# 03 - Add some magic

**NB:** You should use the code and tests from the previous exercises as a starting point instead of the Python files in this directory. 

## Verify that the existing code lives up to the specification

1. Have another look at the requirements and the refactored implementation. If there is any functionality or behaviour missing or untested, apart from the support for conjured items, it is time to write tests for it and make any changes needed.
  * Hint: the original code used hardcoded, full strings to identify backstage passes to a specific concert, but the requirements does not mention that particular concert.

## Add support for conjured items

2. It is finally time to add support for conjured items as per the _gilded_rose_requirements.md_ specification.
  * Practice test-driven development!
    * Start by writing and updating the tests you need to describe and drive the development of this behaviour.
    * Implement the support.
    * When all tests pass, refactor the _structure_ of your code without changing its _behaviour_.

## Bonus round (optional exercises)

3. It would be nice to be able to output a store's items to a file. Write a method in `GildedRose` that allows you to do this.
* Gold star if you practice test-driven development. How can you TDD when writing a file?
  * Hint: have a look at [`tempfile`](https://docs.python.org/3/library/tempfile.html).

4. Another day, another way of exporting the data is requested. This time, the data needs to be in JSON. Add a method for converting a `GildedRose` object into JSON.
* Once again, gold star if you practice test-driven development.

5. Of course someone wants to manipulate the contents of a store using `pandas`. Add a method to export a `GildedRose` instance as a [Pandas `DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).
* Gold star if...well, you know the drill by now.

6. It would change the behaviour to fix it, but the `__repr__` method of the `Item` class does not behave as is conventional for Python classes. What would a idiomatic implementation look like? Remember to write tests before you change the current implementation.
 
## Looking for inspiration?

See [_concepts/leap_year/03a_the_excel_bug.md_](../../concepts/leap_year/03a_the_excel_bug.md).

## Solution notes

A solution for steps 1-2 has been provided in the _solutions/03_add_some_magic_ directory.
