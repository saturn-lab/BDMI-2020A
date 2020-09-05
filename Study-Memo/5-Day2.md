## 大数据与人工智能第二讲

2020/02/26

-----

#### 参考书

THU. library.
https://ebookcentral.proquest.com/lib/tsinghua/home.action

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, Introduction to Algorithms-Third Edition-The MIT Press (2009)

字符串str：
单引号，双引号，或者三个单引号都可以用，字符串不能更改

可以相加，

PEP8:最大是79个字符

str.format()
help（）：帮助如help（str.replace）
str.format()格式化输出
str.join（）字符串连接
+=   =XX+
str.upper(), str.lower(), str.title()：全大写，全小写，每个单词第一个大写
str.strip(): 首尾字符去掉，还有lstrip， rstrip
str.split: 抽取字符串中的一些东西，然后分成一个list

list：用[]，accessing value是顺序，list可变，从第0个开始

if语句：
languages = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
if 'Python' in languages:
    print('Python is there!')
    要空4个空格
list要注意一个问题：比如A 是一个列表 A=B，那么A一直和B等同，而用list（XXX）则是原来创建一个独立的

list.sort（）:从小到大，原地排序，将原列表改变
list.sort（reverse=True）:从大到小
如果排列的是字符串，则用的是字典序
sorted（list）：创建一个新的列表，结果是他们排过序的

逻辑（not,or, and）执行顺序是从左到右，要想控制方向，就用括号
python 一般不用分号，放不放分号都可以执行，只有两条语句放一行里时采用分号。
break 和continue是和C++一样的
enumerate()

range（5）：12345
range(2,5):2345
range(0,10,2):最后一个是步长02468

python里key word都是绿色的
def XXX():
    XXXX
    
函数最后空一行是代表函数结束吗？
默认值：应该就是缺省值了，没有填的话就自动填了
不能用可以改变的东西作为缺省值

docstrings：注释，用三个双引号，当你help(XXX)时候，就打印出来了

pass 执行的时候就是空函数，就是先没弄的时候就占位，后来再填上

类：class XXX:
类 那里 下划线怎么没了

模块： 以py为后缀名
包是包括__init__.py文件，可以承载模块和其他包
别人用的话就是import XX from XXX
XX中比如什么包中的什么用. 小的地方放前面

大数相乘：分治
伪代码：<img src="C:\Users\wangy\AppData\Roaming\Typora\typora-user-images\image-20200226145513850.png" alt="image-20200226145513850" style="zoom:50%;" />

优化：<img src="C:\Users\wangy\AppData\Roaming\Typora\typora-user-images\image-20200226145812430.png" alt="image-20200226145812430" style="zoom:50%;" />

其实运筹学的东西很多都很好啊，都忘了

插入排序和合并排序：

插入排序：后面的数字一个个插到前面

一个算法的两个问题：是否可行？是否快？

是否可行一般用的是归纳假设

合并排序：先分成两个，再挨个比
