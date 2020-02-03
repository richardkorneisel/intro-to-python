# Exercise 1: Most Clocks Are Normal, But Some Are Cuckoo!

**Skill you're Practicing:** Writing Conditionals

For this problem, put your solution into a file called `exercise2.py`.

You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote.

You'll create a variable, `time`, which has an integer value between zero and 23, representing the hour of the day in [military time](https://www.thebalancecareers.com/military-time-3356971), which is a 24-hour clock.

Write a conditional statement with Python code that prints exactly one message using the following rules:

* If the time of day is before 9 a.m. --> print the quote `'Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.'`

* Otherwise if the time of day is before or exactly 4 p.m. --> print the quote `'Working hard or hardly working?'`

* Otherwise, if the time of day is before 8 p.m. --> print the quote `'How did it get so late so soon?'`

* Otherwise, if the time of day is before 10 p.m. --> print the quote `'A day without sunshine is like, you know, night.'`

* Otherwise, for any time 10 p.m. or later --> print the quote `'Burning the midnight oil!'`

## Starter Code

```python
time = 8

# Continue to write more code!
```

> **Hint:** Test your code with different values for time of day. Make sure you are only printing one statement, regardless of the value of `time`!

---

# Exercise 2: I Came, I 'Saur, I Conquered

**Skill you're Practicing:** Writing Conditionals with Multiple Conditions

For this problem, put your solution into a file called `exercise3.py`.

The mighty Tyrannosaurus Rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps!

Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:

* If T-Rex is angry, hungry, and bored he will eat the Triceratops
* Otherwise, if T-Rex is tired and hungry, he will eat the Iguanadon
* Otherwise, if T-Rex is hungry and bored, he will eat the Stegasaurus
* Otherwise, if T-Rex is tired, he goes to sleep
* Otherwise, if T-Rex is angry and bored, he will fight with the Velociraptor
* Otherwise, if T-Rex is angry or bored, he roars
* If T-Rex is none of the above, he gives a toothy smile

## Starter Code

```python
angry = True
bored = True
hungry = False
tired = False

# Example `if` statement
# (This is just an example, you'll have to do much more!)
if bored:
    print('T-Rex roars! RAWR!')
```

---

# All Done!

Now, go be like a T-Rex and do what you please!

![](https://media.giphy.com/media/1NFXnqVxzGr6w/giphy.gif)