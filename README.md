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
function_name, fizzbuzz = p.getFnFromStackOverflow(query="fizzbuzz")  # Get a fizzbuzz function from Stack Overflow
print(p.getHelpText(function_name))  # Get the parameters and function name for fizzbuzz
print(fizzbuzz(3))  # Use the method! Make sure that this variable name is the same as the value of function_name

# Get second smallest number from list
second_smallest_fn = p.addFnFromStackOverflow("find second smallest number in list")
print(p.getFn(second_smallest_fn)([1,2,3,4,5]))  # We can also just use the function directly, without assigning it to a variable name
```