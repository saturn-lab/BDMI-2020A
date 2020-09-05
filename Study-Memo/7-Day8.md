* 自动微分
     * 前向模式：适用于输出多，输入少
     * 反向传播
     
* Tensorflow-more
     
     * 深度学习框架：编程语言、解释器、编译器
     * tensorflow：tensor张量（常量，变量，占位符，rank，shape，datatype）
     * Keras:tensorflow中的库
     * 步骤：选择模型、构建网络、编译、训练、预测
     
* 卷积网络与循环网络

     * 卷积网络：

       好处：并行，减少参数；

       应用：图像识别

     * 循环网络：

       应用：识别，翻译，预测, LSTM；

       特点：参数共享

       问题：梯度消失，梯度爆炸-LSTM                   

* Dense-CNN-RNN

     * MLP:多个Dense组成，常用于分类，激活函数softmax
     * 卷积：减少参数量；卷积层+池化层+丢弃层(减少过拟合问题)
     * RNN：时间步长
     * LSTM：辅助记忆单元+门

