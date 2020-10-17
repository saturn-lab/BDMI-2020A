# 第四周小结(10.6)

#### Bogo Sort

* 期望时间复杂度 $O(n!)$
* 最差情况：$infinite$

#### Quick Sort

* 随机选择pivot，将不大于的元素放置pivot左侧，其余放置右侧，对左右子序列进行递归。
* 期望时间复杂度 $O(nlogn)$
* 最差情况 $O(n^2)$
* $Merge Sort$  的最差情况为 $O(nlogn)$

#### Bucket Sort

* 根据最大值和最小值创建相应个数的”桶“
* 将对应的数据放入”桶“中
* 将桶中元素按顺序合并，完成排序

#### Radix Sort

* 先按照第一位进行桶排序，再按第二位、第三位...进行桶排序，进行到最高位即完成整体排序
* 时间复杂度 $O(nd)$
* r进制时，数据最大值M，时间复杂度为$O((\lfloor log_r (M)\rfloor+1)\cdot (n+r))$
* r越大，”桶“越多，迭代深度越小。

#### 链表

* 插入需要 $O(1)$
* 查找需要 $O(n)$

#### 二叉树

* 二叉树的遍历，修改等基本操作
* 插入、查找、删除需要 $O(logn)$

#### [课堂练习代码](https://github.com/Yuanz233/BDMI-Course/blob/master/Code/Week4.ipynb)





