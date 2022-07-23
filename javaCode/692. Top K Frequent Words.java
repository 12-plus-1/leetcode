class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for (String s : words) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        
        Queue<String> heap = new PriorityQueue<>((o1, o2) -> {
            if (map.get(o1) == map.get(o2)) {
                return o2.compareTo(o1);
            }
            return map.get(o1) - map.get(o2); 
        });
        
        for (String s : map.keySet()) {
            heap.offer(s);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        
        Queue<String> lexiHeap = new PriorityQueue<>((o1, o2) -> {
            return  o2.compareTo(o1);
        });
        
        String[] res= new String[k];
        int p = k - 1;
        for (int i = 0; i < k; i++) {
            String cur = heap.poll();
            if (!lexiHeap.isEmpty() && map.get(cur) != map.get(lexiHeap.peek())) {
                while (!lexiHeap.isEmpty()) {
                    res[p] = lexiHeap.poll();
                    p--;
                }
            } 
            lexiHeap.offer(cur);
        }
        
        if (!lexiHeap.isEmpty()) {
            while (!lexiHeap.isEmpty()) {
                res[p] = lexiHeap.poll();
                p--;
            }
        }
        
        List<String> result = new ArrayList<>();
        for (String s : res) {
            result.add(s);
        }
        
        return result;
    }
}
