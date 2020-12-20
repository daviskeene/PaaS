"""
Python as a Service: Pulling python code from the web and running it!
"""
from bs4 import BeautifulSoup
import urllib.request
from googlesearch import search

class PaaS:
    def __init__(self):
        self.code = {}
        self.params = {}
        self.fns = {}

    def addCode(self, fn_name, params, code):
        self.code[fn_name] = code
        self.params[fn_name] = params

    def addFn(self, fn_name, fn):
        self.fns[fn_name] = fn

    def getFn(self, fn_name):
        if fn_name in self.fns:
            return self.fns[fn_name]

    def addFnFromStackOverflow(self, query):
        # We need to first look up the querystring in a google search
        urls = search(f"stackoverflow python {query}", num=5, stop=10)
        for url in urls:
            # Get the document data at each URL
            webpage = urllib.request.urlopen(url)
            soup = BeautifulSoup(webpage, 'html.parser')
            answer_box = soup.find('div', attrs={'class': 'accepted-answer'})
            if answer_box:
                code = answer_box.find('code')
                if code:
                    fn, params, code = saveToFunction(code.text)
                    if fn:
                        self.addCode(fn, params, code)
                        exec(code)
                        self.addFn(fn, eval(fn))
                        return fn
    
    def getFnFromStackOverflow(self, query):
        fn = addFnFromStackOverflow(query)
        return fn, self.fns[fn]
    
    def getHelpText(self, fn_name):
        if fn_name in self.fns:
            return f"You can use this function like so: {fn_name}({self.params[fn_name]})."
        else:
            return f"Function {fn_name} not recognized, please try again or add it yourself."


def saveToFunction(code):
    """
    Returns the function name and function from stack overflow code.
    """
    # Parse the text to get the function name, and the full method body
    defstart = 0
    defExists = False
    defend = 0

    fn_name = ""
    params = ""

    i = 0
    code_parts = code.split("\n")

    for line in code_parts:
        if line.startswith("def"):
            # Everything after def, and before (
            fn_name = line.split("def ")[1].split("(")[0]
            # Everything inside of ()
            params = line.split("(")[1].split(")")[0]
            defstart = i
            defExists = True
            continue
        elif not line.startswith(" ") and defExists:
            defend = i + 1
            break
        i += 1

    if defend == 0:
        # If that's all she wrote
        defend = len(code_parts)

    if fn_name:
        return fn_name, params, "\n".join(code_parts[defstart:defend])
    return None, None, None


if __name__ == "__main__":
    """
    Just a quick demo :)
    """
    p = PaaS()
    # fizz = p.addFnFromStackOverflow(query="fizzbuzz")
    # fizzbuzz = p.getFn(fizz)
    # # How do we use this function?
    # print(p.getHelpText(fizz))
    # # We can actually use this code now!
    # print(fizzbuzz(3))

    # fib = p.addFnFromStackOverflow(query="fibonacci")
    # F = p.getFn(fib)
    # print(p.getHelpText(fib))
    # print(F(5))
    # print(p.fns[fib])

    # Get second smallest number from list
    second_smallest_fn = p.addFnFromStackOverflow("find second smallest number in list")
    # Find out what to name our function variable
    print(p.getHelpText(second_smallest_fn))
    print(p.getFn(second_smallest_fn)([1,2,3,4,5]))