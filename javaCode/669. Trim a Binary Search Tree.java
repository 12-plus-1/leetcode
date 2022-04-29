// wrong answer


class Solution {
    public TreeNode trimBST(TreeNode root, int low, int high) {
        TreeNode result = trimLow(root, low);
        return trimHigh(result, high);
    }
    
    private TreeNode trimLow (TreeNode root, int low) {
        if (root == null) {
            return null;
        }
        if (root.val >= low) {
            root.left = trimLow(root.left, low);
        }else {
            TreeNode tmp = root.right;
            while (tmp != null && tmp.val < low) {
                tmp = tmp.right;
            }
            return tmp;
        }
        return root;
    }
    
    private TreeNode trimHigh (TreeNode root, int high) {
        if (root == null) {
            return null;
        }
        if (root.val <= high) {
            root.right = trimHigh(root.right, high);
        }else {
            TreeNode tmp = root.left;
            while (tmp != null && tmp.val > high) {
                tmp = tmp.left;
            }
            return tmp;
        }
        return root;
    }
}
