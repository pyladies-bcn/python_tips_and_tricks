# -*- coding: utf-8 -*-

"""
Python tips & tricks. Pyladies January 2015 meetup.

INSTRUCTIONS:

This script contains 4 different classes, each one corresponding to on of the
topics covered in Pyladies January 2015 meetup: unpacking variables, for/in
statements, comprehension lists and lambda functions.

Each class contains functions corresponding to the exercises to solve. Their
docstrings describe what you are suposed to do: refactoring a function, filling
the gaps...

To execute the file:
$ python python_tips_tricks.py

Solve all the exercises in pairs or by yourself, ask all the questions you have
and HAVE FUN!
"""

import sys


class UnpackingVariables:
    """
    """

    def exercise1(self):
        """ Refactor this code so that it doesn't use a third variable.
        Question: can you write it in just three lines?
        """
        var1 = 'a'
        var2 = 'b'

        var3 = var1
        var1 = var2
        var2 = var3

        print [var1, var2]

        print "### not completed ###"

    def exercise2(self):
        """ The range() function expects separate start and stop arguments,
        i.e., range(3, 6). If you have a list of parameters, [3, 6], how can you
        call the range function using this list?
        """
        print range(3, 6)  # normal call with separate arguments
        args = [3, 6]
        # print range(args)  # this doesn't work. How can we fix it?

        print "### not completed ###"

    def exercise3(self):
        """ Execute this script file adding extra parameters like this:
        $ python python_tips_tricks_exercices.py param1 param2 param3
        Now, unpack their values using sys.argv and print the name of the script
        and the values of each extra parameter.
        Tip! Print sys.argv to see what kind of data it returns
        """
        print "### not completed ###"


class ForInStatement:
    """
    """

    def exercise1(self):
        """ Using a for loop, add all the elements in list1 to a new list list2,
        but incrementing each element by 2. Print list2.
        """
        list1 = [1, 2, 3, 4, 5]

        print "### not completed ###"

    def exercise2(self):
        """ Write  a for loop that iterates 5 times, each time printing a line
        with the iteration number, i.e., 'this is iteration number 1'.
        Tip! Remember to use the range() function.
        """
        print "### not completed ###"

    def exercise3(self):
        """ Make a list of the most important words you have learned in
        programming so far.
        Make a corresponding list of definitions (fill it with dummy text).
        Use a for loop to print out each word and its corresponding definition.
        """
        print "### not completed ###"


class ListComprehensions:
    """
    """

    def exercise1(self):
        """ Write out the following code without using a list comprehension:
        plus_ten = [number + 10 for number in range(1, 11)]
        """
        print "### not completed ###"

    def exercise2(self):
        """ Refactor this for/if statement using a comprehension list,
        """
        a_list = [3, 4, 6, 8, 9, 10, 15]
        new_list = []
        for item in a_list:
            if item % 3 == 0:
                new_list.append(item)
        print new_list

        print "### not completed ###"

    def exercise3(self):
        """ Print a list of the squares of even 0-9 using a comprehension list
        Tip! you can get the square of a number with: num ** 2
        Tip! to know if a number is even use: not num % 2
        """
        print "### not completed ###"

    def exercise4(self):
        """ Invert this dictionary dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} using
        a dictionary comprehension.
        The output should be {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        Tip! instead of a list comprehension ([a for a in ...]), use a dictionary
             comprehension ({v:k for v, k in ...})
        Tip! dict.items() is a list of tuples [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
        """
        dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

        print "### not completed ###"

    def exercise5(self):
        """ Given a tuple list, tuple_list = [('A', 10), ('B', 20), ('C', 30)]
        create two separate lists letters = ['C', 'B', 'C'] and
        numbers = [10, 20, 30] using comprehension lists. Print both lists.
        """
        tuple_list = [('A', 10), ('B', 20), ('C', 30)]
        
        print "### not completed ###"

    def exercise6(self):
        """ Given a letters list, letters_list = ['a', 'b', 'b', 'c', 'b'],
        print a list of the position of the letter 'b' in the list.
        The result should be: [1, 2, 4]
        Tip! Remember the function enumerate(list).
        """
        letters_list = ['a', 'b', 'b', 'c', 'b']

        print "### not completed ###"


class LambdaFunctions:
    """
    """

    def exercise1(self):
        """ Write a lambda function x that sums the numbers in range(1, 4), call
        it and print the result.
        """
        # x = ...
        # print x()
        print "### not completed ###"

    def exercise2(self):
        """ Write a lambda function x that add an exclamation sign to a string.
        Using the map function, use you lambda function to apply it to a list of
        strings and print the list.
        Tip! Remember that the map function applies an operation to each item of
        the list and collects the result. If x is your lambda function, you can
        use map like this: map(x, words_list)

        """
        words_list = ['one', 'two', 'three', 'four']
        print "### not completed ###"

    def exercise3(self):
        """ Refactor this code using a lambda function instead of defining
        function key
        """
        def key(x):
            return x[1]

        a = [(1, 2), (3, 1), (5, 10), (11, -3)]
        a.sort(key=key)
        print a

        print "### not completed ###"


def main():

    unpacking_variables = UnpackingVariables()
    print "\n------------------------------------- unpacking_variables\n"
    print "\nunpacking_variables.exercise1"
    unpacking_variables.exercise1()
    print "\nunpacking_variables.exercise2"
    unpacking_variables.exercise2()
    print "\nunpacking_variables.exercise3"
    unpacking_variables.exercise3()

    print "\n------------------------------------- for_in_statement\n"
    for_in_statement = ForInStatement()
    print "\nfor_in_statement.exercise1"
    for_in_statement.exercise1()
    print "\nfor_in_statement.exercise2"
    for_in_statement.exercise2()
    print "\nfor_in_statement.exercise3"
    for_in_statement.exercise3()

    print "\n------------------------------------- list_comprehensions\n"
    list_comprehensions = ListComprehensions()
    print "\nlist_comprehensions.exercise1"
    list_comprehensions.exercise1()
    print "\nlist_comprehensions.exercise2"
    list_comprehensions.exercise2()
    print "\nlist_comprehensions.exercise3"
    list_comprehensions.exercise3()
    print "\nlist_comprehensions.exercise4"
    list_comprehensions.exercise4()
    print "\nlist_comprehensions.exercise5"
    list_comprehensions.exercise5()
    print "\nlist_comprehensions.exercise6"
    list_comprehensions.exercise6()

    print "\n------------------------------------- lambda_functions\n"
    lambda_functions = LambdaFunctions()
    print "\nlambda_functions.exercise1"
    lambda_functions.exercise1()
    print "\nlambda_functions.exercise2"
    lambda_functions.exercise2()
    print "\nlambda_functions.exercise3"
    lambda_functions.exercise3()

    print "\n-------------------------------------\n"

if __name__ == '__main__':
    status = main()
    sys.exit(status)
