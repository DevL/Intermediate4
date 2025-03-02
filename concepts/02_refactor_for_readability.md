# 02 - Refactoring for readability

A refactoring changes _structure_, not _behaviour_. A prime reason for refactoring is to make future changes easier to make. [Kent Beck](https://kentbeck.com) eloquently puts this as "first make the change easy, then make the easy change".

There are many named refactoring moves that can be made. [Martin Fowler](https://martinfowler.com) lists plenty of them in his [catalogue](https://refactoring.com/catalog). Be aware that several of them have different names in other contexts. For example, your code editor may refer to some of them with slightly different names.

## Some refactorings

* Rename
    * variable, e.g. `x` becomes `year`.
    * function, e.g. `process` becomes `process_student_application`.
* extract/introduce variable
* extract/introduce function/method
* replace primitive with object
    * e.g. instead of passing around an `int` denoting a monetary value in cents, we create and use a `Money` class.

## Exercises

See [_exercises/02_refactor_for_readability/instructions.md_](../exercises/02_refactor_for_readability/instructions.md) for the exercises.

## Resources

* Martin Fowler's [refactoring.com](https://refactoring.com) and his [catalogue](https://refactoring.com/catalog).
