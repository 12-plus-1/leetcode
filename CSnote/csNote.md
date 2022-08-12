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
