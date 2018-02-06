# Lab 03 - Working with Higher Order Functions

The purpose of this lab is to practice working with Python's higher order functions and ternary operator. In particular, you will work with:

* Mapping -- see page 196
* Filtering -- see page 197
* Reducing -- see page 197-198
* Lambda -- see page 198

Along with these higher order functions, you'll also implement similar behavior using "list comprehensions." See [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) for more details.

Finally, you'll also work with Python's ternary conditional operator. This operator is dubbed a "ternary" operator because it has three operands. The general form of this operator is:

```python
a if condition else b
```

where `condition` is some expression that evaluates to `True` or `False`. When the `condition` evaluates to `True`, the value `a` is returned; when the `condition` evaluates to `False`, the value `b` is returned.

## Getting Started

As usual, after accepting the GitHub Classroom assignment, clone your repo to your workstation and create a branch named `develop` within which to do your work. Once you have created/checked out your `develop` branch, set out by implementing each function in turn found in the `lab03` module. You can check your progress by either running the `lab03` module and comparing it with the expected output (shown below) or by running the `lab03test` module. Either way, it is recommended that you commit at least after implementing each function.

When all the functions are properly implemented, running the `lab03` module will have the following output:

```
Mapping yields: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
Filtering yields: [3, 6, 9]
Reduce yields: 12345678910
Question 4 - list comprehension = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
Question 5 - list comprehension = [3, 6, 9]
Question 6 - list comprehension = [27, 216, 729]
even_filter(a) = ['four', 'eight', 'ten']
find_min(-3, 4) = -3
find_min(4, -3) = -3
find_min(4, 4) = 4
```

Of course, at this point, all of the unit tests will pass as well.

## Submission Details

This lab is due by 5:00 PM, Tuesday 06 February 2018. As usual, this assignment is submitted by providing a Text Submission on Blackboard that provides the URL for the pull request you created for this lab.