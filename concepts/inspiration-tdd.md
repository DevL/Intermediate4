# Test-driven development (TDD)

From now on you will practice TDD according to the following cycle, called _red, green, refactor_.

## The red-green-refactor cycle

1. Write a failing test for a behaviour you want the code to exhibit.
2. Run the failing test, making note of the information the failure gives you.
3. Add or change _just enough_ code to make the test pass.
    * You may very well need to run the test and add or change code multiple times before the test passes.
    * If you can change code without the test run giving you more information, you are probably lacking a test for that piece of code.
4. Once the test passes, but before you move on to writing the next test, refactor.
    * Refactoring is essential to keep the code moldable and clean.
    * Refactoring does **NOT** include changing behaviour, **ONLY** structure.
    * If you want to change the behaviour, you need to add or change a test as per above.

## Additional Notes

There are volumes written about TDD and how to do it properly. It is the profound conviction and experience of the instructor that professionals write tests before the production code and not the other way around.

Professionals can also add tests after the fact for a legacy system that lacks them. They do so before changing it in order to understand it and create a safety harness to operate from. We will dive into this on day four when we transform a legacy code base.
