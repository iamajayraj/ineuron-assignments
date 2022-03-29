1. What exactly is []?
Ans. [] is basically an empty list.

2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans. spam.insert(3,'hello')

Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
3. What is the value of spam[int(int('3' * 2) / 11)]?
Ans. 3

4. What is the value of spam[-1]?
Ans. d


5. What is the value of spam[:2]?
Ans. [a,b,c]


Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
6. What is the value of bacon.index('cat')?
Ans. 1

7. How does bacon.append(99) change the look of the list value in bacon?
Ans. bacon=[3.14,'cat',11,'cat',True,99]

8. How does bacon.remove('cat') change the look of the list in bacon?
Ans. [3.14, 11, 'cat', True, 99]

9. What are the list concatenation and list replication operators?
Ans. list concatination implies adding or merging two different lists whereas list replication operators include copying a single list multiple times.

10. What is difference between the list methods append() and insert()?
Ans. append() ends the element at the end of the list where as insert takes two parameters index num and element. so it inserts the element at 
a specific index number.

11. What are the two methods for removing items from a list?
l.pop() and remove()

12. Describe how list values and string values are identical.
Ans. 1. list and string both are iterable.
     2. list and string both are made of individual elements

13. What's the difference between tuples and lists?
Ans. lists are mutable but tuples are immutable

14. How do you type a tuple value that only contains the integer 42?
Ans. tup=(42)

15. How do you get a list value's tuple form? How do you get a tuple value's list form?
Ans. tup=tuple(l1) and l1=list(tup)

16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
Ans. ''' I DID NOT UNDERSTOOD THE QUESTION'''

17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans. In copy.copy(), changes made in duplicate copy can also reflect in orignal copy. This specifically occurs in the case of nested lists.
     While copy.deepcopy() makes two seprate copies and change made in one copy do not reflect in other even in the case of nested lists.
