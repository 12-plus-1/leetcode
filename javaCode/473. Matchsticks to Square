class Solution {
    private Map<String, Boolean> memo = new HashMap<>();
    
    public boolean makesquare(int[] matchsticks) {
        int sum = 0;
        for (int i : matchsticks) {
            sum += i;
        }
        if (sum % 4 != 0) {
            return false;
        }
        int edge = sum / 4;
        int[] used = new int[matchsticks.length];
        return backtrack(matchsticks, edge, used, 0, 0, 0);
        
    }
    
    private boolean backtrack(int[] sticks, int edge, int[] used, int counter, int singleEdge, int start) {
        if (counter == 3) {
            return true;
        }
        
        String state = Arrays.toString(used);
        
        if (singleEdge == edge) {
            boolean res =  backtrack(sticks, edge, used, counter + 1, 0, 0);
            memo.put(state, res);
            return res;
        }
        
        if (memo.containsKey(state)) {
            return memo.get(state);
        }
        
        for (int i = 0; i < sticks.length; i++) {
            if (used[i] == 1) {
                continue;
            }
            if (singleEdge + sticks[i] > edge) {
                continue;
            } 
            singleEdge += sticks[i];
            used[i] = 1;
            if (backtrack(sticks, edge, used, counter, singleEdge, i + 1)) {
                return true;
            }
            singleEdge -= sticks[i];
            used[i] = 0;
        }
        return false;
    }
}
