# String
## Method
```java
str.length(); //length of str object is a function
String str = String.valueOf(num); // convert number to String
str.equal(str0); // judge if 2 strings are equal

```


## Reference
### Get one element
```java
str.charAt();
```

### Iteration
```java
for (int i = 0; i < str0.length(); i++) {
    System.out.println(str0.charAt(i));
}
```

### Clip
```java
String slice = str.substring(1, 4);
```

## Convert
### List to String
```java
// only works for char list
char[] list0 = new char[] {'1', '3', '4'};
String str1 = new String(list0);
```
### String to List
```java
String to CharArray:
char[] charList = str.toCharArray();
```
### ArrayList to String
```java
String str = String.join('', list);

```

