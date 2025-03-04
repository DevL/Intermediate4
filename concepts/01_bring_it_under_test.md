# 01 - Bring it under test

When working with legacy code, it is common to make changes or additions that break existing functionality or behaviour. It is even more common to break it in unexpected or unobvious ways.

That is why before we start making changes and additions, we should make sure that our code is under test. Ideally, it was created using test-driven development and in that case we celebrate as we likely have a good amount of the code base covered by tests. Usually, there are no tests at all so we despair instead.

Without tests, we have no safety harness, no guard rails to protect us against making unexpected and undesired changes.

Our first task when confronted with test-less code then, should be to explore and document its current behaviour using tests. In the process of writing tests to describe and document the current behaviour, we will also understand it.

Given untested legacy code, the goal should be to reach a point where it is covered with enough tests for us to practice fearless, test-driven development from that point on.

## The Gilded Rose kata

We will be working with a [code kata](https://en.wikipedia.org/wiki/Kata#Outside_martial_arts) called [_Gilded Rose_](https://github.com/emilybache/GildedRose-Refactoring-Kata) popularized by the eminent [Emily Bache](https://emilybache.com/). Just like the original code kata our starting point is a piece of gnarly, deeply nested, and convoluted code.

Unlike the original code kata, all tests have been removed so that we must write our own. This simulates inheriting a legacy code base devoid of tests. In the first exercise, we will **only** be writing tests. In subsequent exercises we will rely on the tests that we create to refactor the legacy code into something that is much more pleasant to work with. 

## Where to start when adding tests

There are typically two directions one can create tests from: _inside-out_ and _outside-in_.

### Inside-out testing

This type of testing involves identifying small, self-contained pieces of code that can be tested in isolation. A benefit to this approach is that it's usually easier to test this way. A downside is that we run the risk of having a lot of disconnected bits tested, lacking the whole.

A starting place in our case would be to get the `Item` class under test first.

### Outside-in testing 

Outside-in testing starts at the boundaries of the code we want to test. Taking the perspective of a user of our code or system, it is quite common to write a test detailing a number of life-like interactions with the code and then check that all our expectations have been met. Once this test is in place, it is common to dive deeper to detail the interactions and behaviour of the bits and pieces that make up our code.

A starting place in our case would be to write a comprehensive test that creates a `GildedRose` instance, complete with a number of `Item`:s, executes the logic for updating the items, and lastly assert that the new state of our store is as expected.

_The instructor's personal note: I greatly prefer this approach - especially when practicing TDD._

### Where to truly start when adding a test

In our case, the `Gilded Rose` kata comes with a requirements specification. It is a good source to understand the _intention_ of how the code should work. However, it _might_ not be the case that the existing code lives up to the specification. Therefore, it is a good idea to get the actual code's behaviour under test, rather than just basing the tests on the written specification.

That said, once that has been done, making sure that there are tests that follow the specification can be an excellent way of identifying any bugs that may or may not be present in the existing code.

### Test helper functions

Do not hesitate to introduce helper functions to make your tests more readable and less cluttered.

## Exercises

See [_exercises/01_the_gilded_rose/instructions.md_](../exercises/01_the_gilded_rose/instructions.md) for the exercises.
