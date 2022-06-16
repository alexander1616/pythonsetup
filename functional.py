
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


class TestArray:
    def __init__(self):
        self.arr = []

    def flatten_and_sort(self, newArray):
        for item in newArray:
            for i in item:
                self.arr.append(i)
        return sorted(self.arr)

testOOP = TestArray()

'''
Make sure to answer the following questions about your coding process:



How does this solution ensure data immutability?

- pure functions should have no side effects, same input same results
Is this solution a pure function? Why or why not?

- yes for the reasons above, same input same output
Is this solution a higher order function? Why or why not?

- yes mathematical approach, equations can be reused over and over again
- oop we create the world by creating classes and bojects

Would it have been easier to solve this problem using a different programming style?

- different styles can solve it, many ways to approach programming

Why in particular is functional programming a helpful paradigm when solving this problem?

- less side effects
- choose functional programming if changing data in databases
'''