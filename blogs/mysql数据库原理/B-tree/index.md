# B-tree

## 1. 二叉搜索树的不足

![problem_of_binary_search_tree](problem_of_binary_search_tree.svg)

## 2. Remedy of BST

**self-balancing tree**

- red-black tree

- B tree

  B树在降低磁盘IO操作数方面要更好一些（相比于红黑树）

## 3. B-tree

3.1 动图展示B-Tree的**INSERT**操作

  insert "31":

![](BTree.gif)

3.2 时间复杂度

$$
O(log(n))
$$

always for **SEARCH, INSERT, DELETE** operations

