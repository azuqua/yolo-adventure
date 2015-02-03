Autocomplete
============

Implement a program that provides an autocomplete interface via stdin and stdout. Upon start you'll need to read in the import/wordlist.txt, build whatever data structures make sense, and then wait for input on stdin. The user will enter in a series of characters and upon hitting enter should be presented with a lexicographically sorted list of strings (space delimited words) that begin with their input string. After presenting the user with their results the program should once again wait for input on stdin.

To submit the solution please follow these steps.

1. Fork this repository and create a new branch on your copy.
2. Fill in setup.py (Use any dependencies you'd like).
3. Implement your solution in main.py. Think about the environments in which your solution will work best, and in which ones it may not perform well. Consider the time and space efficiencies of your solution as well, you'll be asked to defend your implemenation later. Additionally, given the structure of the input text are there any heuristics that can be applied to optimize your solution?
4. Consider the case where this would be extended to return a list of entire quotes that begin the given substring. How would your implementation handle this scenario when the suffix strings can be much larger with a lot of common characters? Don't worry about implementing a solution for this if your current one doesn't handle this well, but be preparted to discuss your solution with regards to this use case too.
5. Consider the case where in addition to a wordlist you are provided a table mapping words to weights (implemented as a float or double). In this scenario you would be asked to return words ordered by their floating point weight instead of their alphabetical ordering. How would this use case affect your solution?
6. Submit a pull request against the master branch on the Azuqua fork.
