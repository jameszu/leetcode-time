Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
------------------------------------------------------------------
### Idea
Interesting question. We can use either recursion or while loop<br>
for serialize we can do normal preorder traversal. If node is not empty, append node val to list, then call encode left and right. Else add a null value into the list. <br>
for deserialize, we can use iterator or for loop. For each element in the list/string, we see if its the null value, if so we just return none, otherwise we set a treenode at the val and expand left and right nodes.
