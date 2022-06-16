# Char Calculation
## Convert Int into Charlist and Process Single Digit

```java
// num to charlist
int num = 1043;
String strNum = String.valueOf(num);
char[] numList = strNum.toCharArray(strNum);

// do something on charlist
for (int i = 1; i < numList.length; i++) {
  numList[i - 1]++; 
  numList[i] += 3;
}

// charlist to nums
String covStr = String.valueOf(numList);
int result = Integer.parseInt(covStr);
```
