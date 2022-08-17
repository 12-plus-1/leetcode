# JAVA TO PYTHON
## make list/tuple with size

```python
list = [0] * 10;
list = [[0] * 10] * 10

tuple = (0,) * 10
```
## convert number
```python
a = int(7/3)
b = long(7/3)

list = [0, 0, 0]
tup = tuple(list)
list = list(tup)
```
## string and list
string
str = "a string"
| Java      | Python |
| ----------- | ----------- |
| str.charAt(i)      | str[i]       |
| toString   | str(target)        |

use ==

list
list = []
| Java      | Python |
| ----------- | ----------- |
| list.add()    | list.append() |
| list.remove(n - 1)    | list.pop(n - 1) |
| list.get(i)   | list[i] |
| list.size()   | len(list) |
| list2 = list.clone()   | list2 = list[:] |

## sort

## ascii calculation
```python
str = 'brty'
a = 'a'
b = 'b'

c = ord(str[0]) - ord(a)
# result is 1

d = str[0] == b
# result is True
```
## Exponentiation
```python
a = b ** c
```

## logical operator
| Java      | Python |
| ----------- | ----------- |
| &&      | and       |
| ||   | or        |
| !   | not        |
| equals   | is        |

## boolean
| Java      | Python |
| ----------- | ----------- |
| true      | True       |
| flase   | False, None, 0, "", (), []  |

JAVA null is not false but Python null is False

## Stack, Queue, and Deque
```python
# stack
stk = []
sz = stk.size()
topVal = stk.peek()
stk.apppend(1)
stk.pop()

# queue and deque
from collections import queue
q = deque()
sz = q.size()

# push and offer
q.append() # push & offer
q.appendleft()

# pop and poll
q.pop() # pop
q.popleft() # poll

# peek
q[0]
q[-1]

q.reverse()
```

## Hash
map
| Java                                        | Python          |
| ------------------------------------------- | --------------- |
| Map<Integer, Integer> map = new HashMap<>() | dict = {}       |
| put(key, val)                               | dict[key] = val |
| get(key)                                    | get(key)        |
| containsKey(key)                            | key in dict     |
| remove(key)                                 | pop(key)        |
| keySet()                                    | keys()          |
| values                                      | values()        |
| size()                                      | len(dict)       |

set
| Java                                | Python          |
| ----------------------------------- | --------------- |
| Set<Integer,> set = new HashSet<>() | set = {}       |
| add(key)                            | set.add(item) |
| contains(key)                       | key in set     |
| remove(key)                         | remove(item)     |
| size()                              | len(set)       |

## heap

## MAX/MIN Integer
```python
a = float('inf')
b = float('-inf')
```

## MAX/MIN function
```python
a = max(1, 3, 4)
b = min(1, 3, 4)
```
## Random
```python
import random
print(random.random()) # 0 to 1
print(random.randint(a, b)) # random integer from a to b (b included)

```

