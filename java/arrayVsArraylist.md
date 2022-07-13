# Array vs ArrayList

## Create
### Array
```java
int[] array = new int[5];
String[] array = new String[] {"nice", "time", "clem", "maru", "innovation"};

// it is not allowed:
int[] list = new int[];
```
### ArrayList
```java
import java.util.ArrayList;
import java.util.List;

List<Integer> list = new ArrayList<>();
List<String> list = new LinkedList<>();
List<Integer> list = List.of(1, 2, 5);
```
## Reference and Replace
### Array
```java
list[i]
list[i] = 3
```
### ArrayList
```java
list.get(i)
list.set(i, target)
```
## Method
### Array
```java
Arrays.sort(array); // no return
```
[sort comparator](https://www.codejava.net/java-core/collections/sorting-arrays-examples-with-comparable-and-comparator)
```java
Arrays.stream(array).sum() //return summary
```
### ArrayList
```java
list.add(int index, E element)
list.remove(int index)
list.removeAll()
list.clear()
list.size()
list.clone() // return a shallow copy

Collections.sort(list) // no return
```

## Convert
### List to Array
```java
Integer[] array = list.toArray(new Integer[3]);
int[][] array = list.toArray(new int[list.size()][]);
```
### Array to List
```java
List<Integer> list = List.of(array);
```

## duplicate
### Array
```java
int[] list1 = list0; // shallow copy
int[] list1 = new int[] {1, 2, 3};
System.arraycopy(list0, 0, list1, 0, 3) // a source array, the starting position to copy from source array, a destination array, the starting position in the destination array, and the number of elements to be copied

int[] list2 = Arrays.copyOf(list0); // shallow if on an array of non-primitive object types.
int[] list2 = Arrays.copyOfRange(list0, 0, 2); // shallow if on an array of non-primitive object types.
```
### ArrayList
```java
List<Integer> list1 = list0.clone // shallow copy 
List<Integer> list1 = new ArrayList<>(list0); // deep copy
```
## 
```java
Arrays.equals(arr1, arr2);
list1.equals(list2);
```
