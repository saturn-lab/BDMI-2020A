# SQL

structive querying language

SQL有两部分：数据操作语言（查询、修改表格中的数据）、数据定义语言（修改、删除整个表）

product(列1名:string(元组类型)，列2名：float(元组类型))

key: 最小的可以确定每一个元组的数据集合，比如学号是key，班级，姓名不是。		key可以有多个。

![image-20200318142523617](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318142523617.png)

## 查询

select: 把行筛选出来

like: 模糊查询

![image-20200318143210121](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318143210121.png)

distinct: 去除重复

order by: 排序，ASC升序，DESC降序

![image-20200318143355580](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318143355580.png)

![image-20200318143437668](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318143437668.png)

## Foreign key contraints

外键Key

![image-20200318143625942](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318143625942.png)

enrolled表格中存在的才能加入student表

![image-20200318143950670](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318143950670.png)

answer: Product的manufacture; Pname, Price



intersect交集，union并集，union all并集且保留两集合重复元素

count: 数多少种

![image-20200318152151933](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318152151933.png)

sum: 求和

![image-20200318152259209](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318152259209.png)

group by: 合并表格



![image-20200318152559188](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200318152559188.png)

having: 筛选条件，与where相似。where先筛出一个表，having再筛

