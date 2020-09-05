# 第八周

## forward mode

前向传播，适用于输入少，输出多的情况。

对偶数

![image-20200408135721223](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408135721223.png)

写成类似复数形式

## backpropagation

![image-20200408135956310](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408135956310.png)

用输出的某一个值来反向求对所有输出参数的导数

适用于多输入，少输出的情况，用于大部分神经网络。



## 自动微分

见微信群代码



## 各种软件

![image-20200408141958680](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408141958680.png)

### tensorflow

简单，运行速度快

![image-20200408142833803](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408142833803.png)

2.0版本增加了立即执行的功能

2.2版本把std string换成tensorflow tstring

### pyTorch

facebook开发，方向上AI搜索

![image-20200408142609165](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408142609165.png)

### Berkeley Caffe

计算机视觉，GPU加速，编程稍微有点难度

![image-20200408142255566](C:\Users\Felix\AppData\Roaming\Typora\typora-user-images\image-20200408142255566.png)

## CNN/RNN

CNN：计算机视觉对象检测,前馈

RNN：处理序列问题，权重共享，反馈

LSTM：记忆单元、遗忘门、输入门、输出门

Dense:  全连接