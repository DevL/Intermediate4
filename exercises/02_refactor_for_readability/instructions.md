# 02 - Refactor for readability

In this exercise we will use the test cases we created in the last exercise, _01 - Bring it under test_, to act as a safety harness while we refactor the legacy code. We will follow the refactoring rules that we previously got familiar with when practicing test-driven development.

**NB:** You should use the code and tests from the previous exercise as a starting point instead of the Python files in this directory. 

## Refactoring rules

* After making a change to the code, run the tests!
* The tests should _always_ pass. If you make a change that break a test you either:
  * need to revert the change and make a smaller one that does not break the test
  * add or revise a missing or faulty test case
* Only change _structure_, not _behaviour_.
  * The tests should fail if you do. If they do not, you are missing a test case. Add it!

## New rule for the Gilded Rose requirements

Disregard the previous Gilded Rose requirements rule about _not_ making any changes to the `Item` class. 
* As long as you do not break its current public API, i.e. being able to read and write `name`, `sell_in`, and `quality`, and make no changes to the `__repr__` method, you may add additional functionality such as support for comparing two items, e.g. by implementing `__eq__`.
* The _gilded_rose_requirements.md_ file in this directory has been updated to indicate this new rule.

## Refactor the legacy code for readability

**NB:** At this stage, we will _still not_ add support for "conjured items". That will come later in exercise _03 - Add some magic_.

1. This is a very open-ended task, but you should strive to make the code readable and easy to change in the future. At the end of the day, it is all about reshaping the code from its current multi-indented mess into something that at a glance can be understood and added to.

_Remember, readability is subjective. For that reason, it is a **very** good idea to do this exercise in pairs or in a group._ 

A few examples of refactoring moves to make include:
* Extracting shared logic into a function.
* Break out low-level logic into private methods and functions that are called from higher-level logic.
  * _Abstractions flow to the top, details sink to the bottom._
* Extracting a new type of object.
  * Could `MagicItem` be a subclass of `Item`? Would that make sense?
* Moving logic and responsibilities from one place to another.
  * Could `Item` objects know the rules for how they should age? Would that make sense? 

## Looking for inspiration?

See [_concepts/leap_year/02a_leap_year_refactorings.md_](../../concepts/leap_year/02a_leap_year_refactorings.md).

## Solution notes

A solution has been provided in the _solutions/02_refactor_for_readability_ directory.
