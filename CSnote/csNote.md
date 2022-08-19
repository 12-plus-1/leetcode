# CS Note

## Array
### sliding window
For subarray/stirng that satisfies certain requirment

```java
// LC3

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int slow = 0, fast = 0;
        int n = s.length();
        int res = 0;
        while(fast < n) {
            char cur = s.charAt(fast);
            map.put(cur, map.getOrDefault(cur, 0) + 1);
            while (map.get(cur) > 1) {
                char slowChar = s.charAt(slow);
                if (map.get(slowChar) == 1) {
                    map.remove(slowChar);
                }else {
                    map.put(slowChar, map.get(slowChar) - 1);
                }
                slow++;
            }
            res = Math.max(res, fast - slow + 1);
            fast++;
        }
        return res;
    }
}
```

### two pointers
[LC75 sort colors](https://leetcode.com/problems/sort-colors/)

maybe 3 pointers

[LC647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

maybe dp

[LC88 merge sorted array](https://leetcode.com/problems/merge-sorted-array/)

maybe 2 pointers in seperate array

### traverse from right
Usually, use this tech with monotonic stack

```java
// monotonic stack
for (int i = n - 1; i >= 0; i++) {
    int cur = arr[i];
    int record = 0;
    while (!stk.isEmpty() && stk.peek() <= cur) {
        stk.pop();
        record++;
    }
    //do something;
    stk.push(cur);
}
 
```

## Backtrack


| Title             | feature                                                      | method                                           |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------ |
| combination       | unique element, single element used once, pick k from n      | start i + 1, store at end                        |
| combination sum 1 | unique element, single element used many times, sum to target | start i, store at end                            |
| combination sum 2 | repeat element, single element used once, sum to target      | sort, start i + 1, used(b), store at end         |
| combination sum 3 | unique element, single element used once, pick k sum to target, **control path size** | start i + 1, store at end                        |
| subset            |                                                              | start i + 1, store during process                |
| subset2           | repeat element, single element used once, subset             | sort, start i + 1, used(b), store during process |
| permutations      | unique element, single element used once                     | start 0, used(d), store at end                   |
| permutations 2    | repeat element, single element used many times               | start 0, used(b, d), store at end                |
|                   |                                                              |                                                  |
|                   |                                                              |                                                  |


