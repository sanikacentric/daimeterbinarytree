class TreeNode :
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def diameter (self,curr :TreeNode )->int :
            self.res =0

            def dfs(curr): ######this function returns height
                 if not curr :
                      return 0
                 left = dfs(curr.left)
                 right =dfs(curr.right)

                 self.res = max(self.res, left+right)

                 return 1+ max(left. right)
            
            dfs(curr)
            
            return self.res
                 




