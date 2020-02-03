# Booleans

## `True` and `False`

"Yes" in computer-speak is **true**, and "No" in computer-speak is **false**.

The boolean data type allow us to represent the concepts of **true** and **false**.

In Python the first letter is capitalized: `True` and `False`.

Boolean expressions are a basic idea in programming, and allow computers to evaluate statements as being either true or false.

```python
store_open = True
student_graduated = False
```

Now that we know how a computer says "Yes" or "No", we can bring in comparisons and logic.

## Comparison Operators

Comparison operators takes two pieces of data and compares them. Mostly we'll be comparing strings and numbers.

* Equality: `==`
* Inequality: `!=`
* Less than: `<`
* Greater than: `>`
* Less than or equal to: `<=`
* Greater than or equal to: `>=`

When you compare two values, you get a Boolean result!

```python
print('3 < 5 is...', 3 < 5)         #--> prints True
print('13 >= 13 is....', 13 >= 13)  #--> prints True
print('50 > 100 is...', 50 > 100)   #--> prints False
print("'d' < 'a' is...", 'd' < 'a') #--> prints False
```

Results from comparisons can be saved in a variable, if you wish:

```python
current_time = 1000
closing_time = 1700
store_open = current_time < closing_time
#--> store_open contains True
```

## Logical Operators

Booleans can be combined with **logical operators**. The three most common are:

* `or`
* `and`
* `not`

### Truth Table for `or`

`or` checks if either side is `True`.

In the following table, `Z = A or B`

![](assets/or.png)

In this example, I'm happy if I get chicken for dinner, **OR** if I get pizza for dinner. (Or both chicken and pizza!!!)

```python
got_chicken = True
got_pizza = False
happy = got_chicken or got_pizza
#--> True

got_chicken = False
got_pizza = True
happy = got_chicken or got_pizza
#--> True
```

### Truth Table for `and`

`and` checks if **both** sides is `True`.

In the following table, `Z = A and B`

![](assets/and.png)

In this example, I'm so demanding that I'm only happy if I get **BOTH** sushi and burgers for dinner. Just one will not satisfy me.

```python
got_sushi = True
got_burgers = False
happy = got_sushi and got_burgers
#--> False

got_sushi = True
got_burgers = True
happy = got_sushi and got_burgers
#--> True
```

### Truth Table for `not`

`not` simply inverts the value of a boolean.

In the following table, `Z = not(A)`

![](assets/not.png)

```python
store_open = True
print(store_open)      #--> True
print(not(store_open)) #--> False
```

```python
student_graduated = False
print(student_graduated)      #--> False
print(not(student_graduated)) #--> True
```

## Truthiness and Falsiness

Something that's `True` is always **true**, right?

```
Yes, I totally cleaned my room.

Just don't look under the bed…
```

Beyond the absolute `True` and `False`, there is a concept of "**truthiness**" and "**falsiness**".

Sometimes, we need "**truthy**" and "**falsy**". They're not explicitly `True` or `False`, but basically behave in the same way.

To know if some piece of data is truthy or falsy, you can try to convert it to a boolean with `bool()`.

* All numbers are Truthy except 0

   ```python
   bool(5)       #--> True
   bool(-5)      #--> True
   bool(0)       #--> False
   bool(0.0)     #--> False
   ```

* All strings are truthy except the empty string

   ```python
   bool('Hello') #--> True
   bool('')      #--> False
   ```

* The special `None` datatype is always falsy.

   ```python
   bool(None)    #--> False
   ```

Another way to think about truthy or falsy is the idea of "presence" (truthy) vs "absence" (falsy). It just means "Is there anything there?"

In Python, the only values that are falsy besides `False` are: `None`, zero (`0`, `0.0`), the empty string (`""`), and empty lists (`[]`), tuples (`()`), or dictionaries (`{}`) - but those last three touch on concepts we won't be talking about for a while, so just put that in your back pocket for now.