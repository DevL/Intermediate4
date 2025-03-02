# 01 - Bring it under test

There are hardly any tests for the legacy code in the file _gilded_rose.py_.
In this set of exercises you will be writing tests in order to cover all the requirements detailed in _gilded_rose_requirements.md_.
You can use the example tests in the _tests_ directory as a starting point, but you should feel free to organise the tests in any way you like. Do not be shy to split and group tests in multiple test modules for example.

Since we not yet have the tests to guard and guide us during the refactoring of the legacy code, it is important to be **very** mindful **not** to change any untested code. This exercise is all about building the guard rails we need to confidently and fearlessly refactor the legacy code in the next exercise: _02 - Refactor for readability_.

Even if it is tempting to implement equality methods for the `GildedRose` and `Item` classes at this point, try to refrain from it. That will be a part of next exercise when we refactor the tests and the legacy code.

**NB:** This is a **very** good opportunity to work in pairs or groups. Make sure to rotate who is writing tests!

## Read the requirements

1. Study _gilded_rose_requirements.md_. That document details the intended behaviour of the code.
  * **NB:** We add a rule about _not_ making any changes _yet_ to the legacy code. We will come back to that in the next exercise, _02 - Refactor for readability_.
  * **NB:** At this stage, we will _not_ add support for "conjured items". That will come later in exercise _03 - Add some magic_.

2. Study the code in _gilded_rose.py_. Does its behaviour match the requirements?

## Build a safety harness

3. Based on the requirements _and_ the existing code, write tests to capture the _current_ behaviour.
  * If the requirements and the actual code's behaviour differ, add an intentionally failing test for it, but mark it using `pytest.mark.xfail` as such.
4. When you feel confident that you have covered all the expected and current behaviour with tests, compare your tests with another student. Discuss what, why, and how you test the various behaviours.
  * If you are working in pairs or groups, this will come naturally. Make sure to rotate who explains a given test case!

## Looking for inspiration?

See [_concepts/leap_year/01a_bring_leap_year_under_test.md_](../../concepts/leap_year/01a_bring_leap_year_under_test.md). 

## Resources

* A [short video](https://www.youtube.com/watch?v=Mt4XpGxigT4) by Emily Bache on why the Gilded Rose kata is so appreciated.
* [The full kata in many languages](https://github.com/emilybache/GildedRose-Refactoring-Kata)

## Solution notes

A solution has been provided in the _solutions/01_the_gilded_rose_ directory.
