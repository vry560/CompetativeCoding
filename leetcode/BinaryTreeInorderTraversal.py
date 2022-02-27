class Solution {
    public List<Integer> res = new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return res;
    }
    
    private void inorder(TreeNode root){
        if(root != null){
            inorder(root.left);
            res.add(root.val);
            inorder(root.right);     
        }
    }
}
