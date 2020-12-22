# 课程大作业说明

## 内容描述

截止日期：2021/1/10（暂定）

##  数据集 

24句语音指令的语音频谱数据集(spectrogram)，语音数据集中包括：

40个人的人声语料数据集，20个人的人声验证数据集。 

频谱图数据集：https://cloud.tsinghua.edu.cn/f/db9d627e4b5d4978973f/

请同学们拷贝这个数据集即可。

## 课程大作业的内容

在输出频谱图数据集上，通过设计深度神经网络模型，得出预测结果。 

分类过程的几种参考方案

（1）建议，分类过程参考链接：https://tensorflow.google.cn/tutorials/images/classification （较方便，推荐。）

（2）分类过程，也可以参考链接：https://tensorflow.google.cn/tutorials/load_data/images  （你还掌握了制作tf.data数据集过程！）

（3）分类过程，也可以参考（谷歌simpleAudio）项目链接：https://tensorflow.google.cn/tutorials/audio/simple_audio
（谷歌TensorFlow官方提供的一个详细从语音文件（*.wav）到时频图（spectrogram），再进行分类的案例。）（你还掌握了从波形文件到时频谱图的制作过程！）

*提示：

可能需要数据增强，进行resize标准大小等方法，来解决过拟合问题，参考链接：https://tensorflow.google.cn/tutorials/images/data_augmentation

网络模型参考一下audioNet项目。项目网页链接：https://github.com/saturn-lab/audioNet 

## 提交实验报告
包括：
- 实验代码验收 (notebook, )
- 模型识别准确度 （训练准确度）
- 给定一个测试集（提交识别结果）
- 实验报告 1 份（列出你的创新点和工作内容）

## 组织方式
（原则上以个人为单位）

（特殊情况，可以申请两人一组，需注明分工）

## 评分标准
每位同学找相应老师验收，验收主要看代码运行和训练过程。验收完的，得合格；

实验报告和模型准确度，得加分。


# 替代性作业
与教师协商。


# 补充说明

原始语音数据集，网页链接：https://cloud.tsinghua.edu.cn/f/601fa559fe02477c8f44/

频谱图生成audioPlot项目。项目网页链接： https://github.com/saturn-lab/audioPlot


