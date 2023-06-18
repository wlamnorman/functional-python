# Functional python
The use for this workspace is to fiddle around with functional programming in Python.

### Contents:
- `functional_programming_with_python_course`: LinkedIn learning course exercises
- `fractals`: playing around with functional programming to create fractals

### Notes
* Functional programming (FP) is imperative unlike object-oriented programming (OOP) which is declarative.
* Key concepts related to FP are
    - *Immutability*: we treat variables as mathematical constants, not as pointers.
    - *Separation of data and functions*: In OOP functions are methods, that is, functions that act on pre-defined objects. In FP functions are separate entities.
    - A pre-requisite for FP is that the programming language treats functions as *First-class functions* meaning that functions can be 1. assigned to variables, 2. arguments to other functions, 3. functions can be returned by themselves (recursively) or other by functions; 4. included in any data structure.
    - *Closure*: Defining a function inside another function allows the inner function to access the outer functions input parameters. When working with nested functions, the use of `nonlocal` can come in handy to declare that a variable is not local, this can be used inside the nested function to tell the interpreter that the variable should not belong to the inner function but rather the outer function. See `02_05.py` for an example.
    - *Higher-order functions* are functions that take functions as arguments or return functions
    - *Partial application* is the process of fixing a number of arguments to a function, producing another function of smaller arity (with less input variables). See `partial_application.py` for an example.
    - *Currying*: Expressing a mutlivariable function, for example $f: X, Y, Z$, as a sequential application of single variable functions, that is $`f(x,y,z)` = \alpha(x, \beta(y, \gamma(z)))$. See `currying.py` for an example.