1. What does an empty dictionary's code look like?
Ans. dict={}

2. What is the value of a dictionary value with the key 'foo' and the value 42?
Ans. 42

3. What is the most significant distinction between a dictionary and a list?
Ans. A dictionay stores elements in key-value pair where list stores value in form of elements.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans. None

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Ans. Basically, ther is no difference as cat in spam will look for cat in key values of spam.
    Also, cat in spam.keys() will also look for cat in keys of spam.
    
6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
Ans.cat in spam will look for cat in key values of spam but cat in spam.values() will look for cat in values of spam.

7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'
Ans. spam.update(color='black')

8. How do you "pretty print" dictionary values using which module and function?
Ans. pprint.pprint() is the code where pprint is the module name and pprint() is the function name.
