# 课程大作业说明

内容描述：语音识别实验和图像识别

语音数据集，网页链接：https://cloud.tsinghua.edu.cn/f/601fa559fe02477c8f44/

频谱图生成audioPlot项目。项目网页链接： https://github.com/saturn-lab/audioPlot

## 步骤1：制作数据集

24句语音指令的语音频谱数据集(spectrogram)，语音数据集中包括：

40个人的人声语料数据集，20个人的人声验证数据集。

请同学们创建一个数据集。

*提示：

建议使用tf.data接口，图像集制作参考链接：https://tensorflow.google.cn/tutorials/images/classification

建议使用tf.data接口，图像集加载参考链接：https://tensorflow.google.cn/tutorials/load_data/images

## 步骤2：课程大作业

在输出频谱图基础上，进行resize标准大小，通过卷积与循环网络得出预测结果。 

网络模型参考一下audioNet项目。项目网页链接：https://github.com/saturn-lab/audioNet 

*提示：

可能需要数据增强来解决过拟合问题，参考链接：https://tensorflow.google.cn/tutorials/images/data_augmentation

## 提交实验报告
- 实验报告1份
- 实验代码验收
- 模型识别准确度

（原则上以个人为单位）

（特殊情况，可以申请两人一组，需注明分工）

