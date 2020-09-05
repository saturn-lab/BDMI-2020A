# 第六次课程小结
## SQL-III
+ 嵌套查询，函数套函数的形式：g(f(x))
+ group-by比嵌套查询更有效率
+ 需要生成set的时候记得distinct
### 关系代数 relational algebra
+ selection $\sigma$
+ projection $\Pi$
+ cartesian product $\times$
+ union $\cup$
+ difference -
## 数据库
### IO model
+ 比起disk，main memory更快
+ page：一个固定大小的存储单元，作为计量单位使用
+ file/read/flush
### External merge
+ 用来将两个排好序的数列合并成一个
+ 更适合处理数据非常大的情况，方法类似归并排序
## 索引
+ simple scan：O（N）
+ binary search：O（$log_2n$）
### B+ tree
+ 基本结构与之前数据结构讲的B树类似
+ 叶子结点有指向下一个节点的指针
+ 如何确定树的d？根据size计算，keys和pointers占的空间应当小于block size
### Cost model
+ 可以储存$(averagefanout)^{height}$条记录
+ 填充因子一般取2/3
+ 精确查找中，聚集索引和非聚集索引没有太大区别；范围查找中，顺序输入输出更快

## 作业回顾
+ problem1
	先算两端的平方然后步步逼近
+ problem2
	+ 宽度优先搜索：遍历矩阵找到O点，之后检查O点四周元素，比较后更新距离，正确性明显，使用更加普遍
	+ 动态规划遍历两遍即可得到结果，但正确性需要证明。
	+ 算法复杂度估计：看点被更新的次数










