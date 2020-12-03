# Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000 <br>

## Idea
Just a while loop or for loop is fine

## Code

```python
# if this null node was a left child, tail is its parent
        # if this null node was a right child, tail is its parent's parent
        if not root: return tail

        # recursive call, traversing left while passing in the current node as tail
        res = self.increasingBST(root.left, root)

        # we don't want the current node to have a left child, only a single right child
        root.left = None

        # we set the current node's right child to be tail
        # what is tail? this part is important
        # if the current node is a left child, tail will be its parent
        # else if the current node is a right child, tail will be its parent's parent
        root.right = self.increasingBST(root.right, tail)

        # throughout the whole algorithm, res is the leaf of the leftmost path in the original tree
        # its the smallest node and thus will be the root of the modified tree
        return res
```