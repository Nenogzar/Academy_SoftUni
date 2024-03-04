<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">

<table>
  <tr>
    <th><img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/image/13.jpg" alt="Dictionary" width="400"></th>
  </tr>
  <tr>
    <td>
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/01_Dictionaries%20-%20Lab">Lab</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/02_Dictionaries%20-%20Exercise">Exercise</a>
  | 
  <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/03_Dictionaries%20-%20More%20Exercises">More</a>
    </td>
  </tr>
</table>

* [Dictionary Definition](https://realpython.com/python-dicts/);
* [Keys and Values](https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/);
* [Iterating Through Dictionaries](https://realpython.com/iterate-through-dictionary-python/);
* [Existence in Dictionaries](https://pieriantraining.com/how-to-check-if-a-key-exists-in-a-python-dictionary/);
<details><summary> 🏛️ Built-in Dictionary Methods 🐍</summary>

#### To illustrate the methods I will use this one dictionary:

```Python
d = {'a': 10, 'b': 20, 'c': 30}
```
<details><summary>🏛️ clear() - Clears a dictionary.</summary>

> clear() empties dictionary d of all key-value pairs:

```Python
d.clear()
print(d)
# {}
```
</details>
<details><summary>🏛️ copy() - Copy a dictionary.</summary>

> The copy() method returns a copy of the specified dictionary.

```Python
x = d.copy()
print(x)
# {'a': 10, 'b': 20, 'c': 30}
```
</details>



<details><summary>🏛️ get(key[, default]) - Returns the value for a key if it exists in the dictionary</summary>

>⚠️ get(key) searches dictionary d for key and returns the associated value if it is found.<br>
If key **is not found**, it returns **None**:


```Python
print(d.get('b'))   
# 20
print(d.get('z'))
# None

```
</details>

<details><summary>🏛️ items() - keys() - values()</summary>

<details><summary>⛓️ items() - Returns a list of key-value pairs in a dictionary</summary>
>items() returns a list of tuples containing the key-value pairs in d. <br>
The first item in each tuple is the key, and the second item is the key’s value:

```Python
list(d.items())
#  [('a', 10), ('b', 20), ('c', 30)]

list(d.items())[1][0]
#  'b'

list(d.items())[1][1]
#  20
```
</details>

<details><summary>⛓️ keys() - Returns a list of values in a dictionary.</summary>

>d.values() returns a list of all values in d:

```Python
print(list(d.keys()))
# ['a', 'b', 'c']
```
</details>
<details><summary>⛓️ values() - Returns a list of values in a dictionary.</summary>

>d.values() returns a list of all values in d:

```Python
print(d.values())
# [10, 20, 30]
```
Any duplicate values in d will be returned as many times as they occur:
```Python
d = {'a': 10, 'b': 10, 'c': 10}
print(d.values())
# [10, 10, 10]
```

</details>

> Technical Note: The .items(), .keys(), and .values() methods actually return something called a view object. A dictionary view object is more or less like a window on the keys and values. For practical purposes, you can think of these methods as returning lists of the dictionary’s keys and values.

</details>
<details><summary>🏛️ fromkeys()- Returns a dictionary with the specified keys and the specified value</summary>

> The fromkeys() method returns a dictionary with the specified keys and the specified value

```Python
y = 0
thisdict = dict.fromkeys(x, y) 
print(thisdict)
# {'a': 0, 'b': 0, 'c': 0}
```
</details>
<details><summary>🏛️ pop(key[, default]) - Removes a key from a dictionary, if it is present, and returns its value.</summary>


>If key is present in d, d.pop(key) removes key and returns its associated value:

```Python
d.pop('b')
# 20

print(d)
# {'a': 10, 'c': 30}
```
>💣 d.pop(key) raises a KeyError exception if key is not in d:

```Python
d.pop('z')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.pop('z')
KeyError: 'z'
```
> If key is not in d, and the optional **default** argument is specified, then that value is returned, and no exception is raised:
```Python
d.pop('z', -1)

print(d)
# {'a': 10, 'b': 20, 'c': 30}
```
</details>

<details><summary>🏛️ popitem() - Removes a key-value pair from a dictionary.</summary>

>d.popitem() removes the last key-value pair added from d and returns it as a tuple:

```Python
d.popitem('c', 30)
print(d)
# {'a': 10, 'b': 20}

d.popitem('b', 20)
print(d)
# {'a': 10}
```
> 💣 If d is empty, d.popitem() raises a KeyError exception:
 
```Python 
d = {}
d.popitem()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
```
</details>
<details><summary>🏛️ update(obj)- Merges a dictionary with another dictionary or with an iterable of key-value pairs.</summary>

> If **obj** is a dictionary, **d.update(obj)** merges the entries from <obj> into d. For each key in **obj**:<br>
> * If the key is not present in d, the key-value pair from <obj> is added to d.<br>
> * If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.<br>
> Here is an example showing two dictionaries merged together:<br>

```Python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
```
In this example, key 'b' **already exists in d1**, so its value is **updated to 200**, the value for that key from d2. 
However, there is no key 'd' in d1, so that key-value pair is **added from d2**.

> obj may also be a sequence of key-value pairs, similar to when the dict() function is used to define a dictionary. 
> For example, obj can be specified as a list of tuples:
```Python
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
print(d1)
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
```
> Or the values to merge can be specified as a list of keyword arguments:
```Python
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
print(d1)
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
```
</details>

<details><summary>🏛️ setdefault() -  Returns the value of the item with the specified key</summary>

>If the key does not exist, insert the key, with the specified value, see example below

> Parameter Values

|Parameter|Description|
|-|-|
|keyname|Required. The keyname of the item you want to return the value from|
|value|Optional.<br>If the key exist, this parameter has no effect.<br>If the key does not exist, this value becomes the key's value<br>Default value None|


```Python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
# Mustang
```
> **Example:** Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

```Python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)
# White
print(car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
```
</details>



</details>
</body>
</html>
