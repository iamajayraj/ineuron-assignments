1.What are the two values of the Boolean data type? How do you write them?
Ans. True and False are two boolean data type where true also means 1 and false also means 0.

2. What are the three different types of Boolean operators?
Ans. AND, OR and NOT

3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
Ans. AND OPERATOR
     0 0 0
     0 1 0
     1 0 0
     1 1 1

     OR OPERATOR
     0 0 0
     0 1 1
     1 0 1
     1 1 1

     NOT OPERATOR
     0 1
     1 0
     
4. What are the values of the following expressions?
Ans. (5 > 4) and (3 == 5)
     False
     not (5 > 4)
     False
     (5 > 4) or (3 == 5)
     True
     not ((5 > 4) or (3 == 5))
     False
    (True and True) and (True == False)
    False
    (not False) or (not True)
    True

5. What are the six comparison operators?
Ans. a==b means a is equal to b
     a!=b means a is not equal to b
     a>b means a is greater than b
     a<b means a is less than b
     a>=b means a is greater than or equals to b
     a<=b means a is less than or equals to b
     
6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
Ans. In assignment operator, single equals to sign is used where as in equal to, doubls equals to is used.
     While storing a data in a variable we use a assignment and while comparing something we use equal to.

7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam=int(input())
if spam==1:
    print('Hello')
if spam==2:
    print('Howdy')
else:
    print('Greetings!')

9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans. ctrl+c

10. How can you tell the difference between break and continue?
Ans. break will break the loop and come out while continue will continue the loop without doing anything.

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans. In python, range function takes three parameters(start, stop, jump).By default the start is 0 and jump is 1. we can initiate range with just one parameter i.e. stop point.
So, range(10), range(0,10) and range(0,10,1) are similar to each other.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1,11):
    print(i)

x=1
while x<=10:
    print(x)
    x=x+1

    
13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
