# Java Hash
## Create
```java
Map<String, Integer> map = new HashMap<>();
Set<Integer> set = new HashSet<>();
```

## Add item
```java
map.put(str, num);
map.putIfAbsent(key, value)

set.add(num);
```

## Contains
```java
map.containsKey(str);
set.contains(num);
```
## Remove item
```java
map.remove(key);
set.remove(item);
```

## Access item
```java
map.get(key);
map.getOrDefault(key, default); // return value of key or default value if key is not existed.

set.get(item);
```

get all item
```java
// Print keys
for (String i : capitalCities.keySet()) {
  System.out.println(i);
}

// Print values
for (String i : capitalCities.values()) {
  System.out.println(i);
}
```

```java
for (String i : cars) {
  System.out.println(i);
}
```



