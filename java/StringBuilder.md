# StringBuilder
[link](https://www.w3schools.blog/stringbuilder-in-java)

## Construct
```java
StringBuilder sb = new StringBuilder() // empty string
StringBuilder sb = new StringBuilder(int capacity) // empty but with certain size
StringBuilder sb = new StringBuilder(String str) // start from a string 
```

## length
```java
sb.length();
```

## method
```java
sb.append(String / char); // str or char
sb.delete(int start, int end);

sb.insert(int offset, String str);
sb.replace(int start, int end, String str);

sb.reverse();
sb.capacity();

```
