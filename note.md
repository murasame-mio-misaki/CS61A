# CS61A

## Welcome&Function 

loop `for` in python, do not forget to add `range ` .

```python
for i in range(a,b): #a included, b excluded (actually [a,b+1])
```

reverse string:

```python
[::-1]
```



## Control&Higher order function

to check a function's docstring:

```python
help(func)
```

and type q to exit.

 lambda expression:

```python
[expression name]=lambda [parameters]:[value] 
```

In python, functions can also be parameters of other functions.



### Hog

Rules: Dice game.

On each turn, the current player chooses some number of dice to roll together, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

- **Sow Sad**. 
- **Boar Brawl**.
- **Sus Fuss**.

example of `assert` checkers:

```python
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
```



*args syntax is used for the function that has arbitrary numbers of args.

Ex: in problem 8:

```python
def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
   
    def func(*args):
        sum = 0

        for i in range(times_called):
            sum += original_function(*args)
        
        return sum/times_called
    
    return func
```

 We don't precisely know how many parameters the `original_function` needs, so we use `*args`.
