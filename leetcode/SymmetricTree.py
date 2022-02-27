class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mroot = self.mirror(root)
        return self.tree_compare(root, mroot)
        
        
    
    def mirror(self, root):
        if root == None:
            return None
        mroot=TreeNode()
        if root.left != None:
            mroot.right = self.mirror(root.left)
        if root.right != None:
            mroot.left = self.mirror(root.right) 
        mroot.val = root.val
        return mroot
    
    def tree_compare(self, root, mroot):
        
        if root == None and mroot == None:
            return True
            
        if root != None and mroot != None:
            isChildSymmetry = self.tree_compare(root.left, mroot.left) and self.tree_compare(root.right, mroot.right) 
            if isChildSymmetry:
                return isChildSymmetry and root.val==mroot.val
        return False
