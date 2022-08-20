# String
## Method
```java
str.length(); //length of str object is a function
String str = String.valueOf(num); // convert number to String
str.equals(str0); // judge if 2 strings are equal

```


## Reference
### Get one element
```java
str.substring(1, 2);
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
### CharList <-> String
```java
// only works for char list
char[] list0 = new char[] {'1', '3', '4'};
String str1 = new String(list0);
```
```java
String to CharArray:
char[] charList = str.toCharArray();
```

### String.join()
array/arraylist to a string
```java
List<String> arrlist = List.of("abc", "ert", "tyr");
String[] arr = new String[]{"ert", "543"};
String str = String.join("", arr); // not applicable for char[]
String str = String.join("", arrlist);
```

### String.split()
String to an array
```java
String str = "geekss@for@geekss";
String[] arrOfStr = str.split("@", 2);
```

### char to String
Character.toString()
```java
String str = Character.toString(chr);
```
### int to String
String.valueOf()
```java
String str = String.valueOf(val);
```
### String to int
Integer.valueOf()
```java
int val = Integer.valueOf(str);
```


