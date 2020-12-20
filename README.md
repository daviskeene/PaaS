# Python as a Service
---

Over the past decade, countless python code snippets have been uploaded to Stack Overflow, containing functions and the way that they should be used.
Developers have been taking advantage of this by googling their python programming questions and copying these functions into their own codebase.

What if, however, this process was streamlined? What if we can grab code from stack overflow and incorporate it into our own projects all inside our own codebase,
without needing to ever open google?

My solution: `PaaS` (Python as a Service), a module that allows you to pull python methods from the web and use them accordingly.

## Example
```python

p = PaaS()  # Create a new Python as a Service class
fizzbuzz = p.getFnFromStackOverflow(query="fizzbuzz")  # Get a fizzbuzz function from Stack Overflow
print(fizzbuzz(3))  # Use the method! Make sure that this variable name is the same as the value of function_name

# What functions are available to us?
p.printFns()  # Prints 'fizzbuzz'

# Get second smallest number from list
second_smallest_fn = p.addFnFromStackOverflow("find second smallest number in list")

# Using the function without first assigning it to a variable name
print(p.getFn(second_smallest_fn)([1,2,3,4,5]))  # Prints 2

# Or, we can accomplish the above in one line (not possible for recursive functions)
print(p.getFnFromStackOverflow("find second smallest number in list")([1,2,3,4,5]))  # Prints 2
```