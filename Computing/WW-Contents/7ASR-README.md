# 语音识别

## 目录

 [[显示](http://wiki.icenter.tsinghua.edu.cn/icenterwiki/index.php/语音识别#)] 

# 语音识别

自动语音识别(Automatic Speech Recognition，简称ASR)技术是使人与人、人与机器更顺畅交流的关键技术

## 研究方法

过去，利用高斯混合模型（Gaussian Mixture Model, 即GMM）以及隐马尔科夫模型（Hidden Markov Model, 即HMM）实现了大词汇量级下的连续语音识别（Large Vocabulary Continuous Speech Recognition, 即LVCSR）。传统使用HMM和GMM混合，其中HMM用来规范时间的变化，GMM用来计算HMM之中各个组合的可能性。

深度神经网络（DNN）与隐藏马尔科夫模型（HMMs），上下文相关模型（context-dependent phone models），n-gram 语言模型（n-gram language models）和维特比搜索算法（Viterbi search algorithms）进行混合使用。

当下，采用了混合方法来构建语音识别引擎，混合模型比较复杂，需要一套精致的训练方法，以及相当多的专业知识来帮助搭建模型。

**传统方法综述**

1. S. Karpagavalli and E. Chandra. "A Review on Automatic Speech Recognition Architecture and Approaches." International Journal of Signal Processing, Image Processing and Pattern Recognition 9, No. 4 (2016): 393-404.

## 语音文件预处理

- SOX程序用于对原始语音录音文件进行添加噪声、混响等扰动信号，增加可供训练的样本数目。

SOX [SOX_CODE](http://sox.sourceforge.net/)

- ffmpeg程序用于对各种格式的录音文件，如*.m4a, *.wav, *.mp3, *,mp4, *.3gpp等，进行统一的转换为*.wav格式的数据，便于统一处理。

ffmpeg [FFMPEG](https://ffmpeg.org/)

# 深度学习方法

深度学习采用一种通用的神经网络来替代复杂的，多维度的机器学习方法。这些神经网络经过训练以后，可以用来优化可微分的代价或损失函数（loss/cost function）。这种方法已经在语音识别上取得了巨大的成功，也称为「纯正」的 DNN 方法。

只要拥有了相当多的训练数据和足够的计算资源，就可以构建一个高水准的大词汇量连续语音识别（Large Vocabulary Continuous Speech Recognition (LVCSR)）系统。

## 神经网络架构单元

### LSTM

- Long short term memory recurrent network(LSTM)

1. Long short term memory neural computation, Neural computation 9 (8), 1735-1780, 1997. [LSTM](http://ieeexplore.ieee.org/document/6795963)

### CTC

- Connectionist temporal classification(CTC)

1. Connectionist temporal classification:labelling unsegmented sequence data with recurrent neural networks, ICML 2006.
2. Sequence Modeling With CTC, https://distill.pub/2017/ctc/.

### GRU

- Gated Recurrent Unit(GRU)

1. On the Properties of Neural Machine Translation Encoder-Decoder Approaches, SSST-8, 2014.

## Alex Graves

[Alex Graves](http://www.cs.toronto.edu/~graves/)，Google DeepMind研究员，语音识别多项技术开创者

- Connectionist temporal classification labelling unsegmented sequence data with recurrent neural networks, ICML 2006.Speech recognition with deep recurrent neural networks, ICASSP 2013.Hybrid speech recognition with deep bidirectional LSTM, ASRU 2013.Towards End-To-End Speech Recognition with Recurrent Neural Networks, ICML 2014.

# 研究进展

## Google

### Google Speech

1. Google AI Blog: An All-Neural On-Device Speech Recognizer, https://ai.googleblog.com/2019/03/an-all-neural-on-device-speech.html.
2. Google Speech Processing from Mobile to Farfield, CHiME 2016. [Google_Speech_Processing](http://spandh.dcs.shef.ac.uk/chime_workshop/presentations/CHiME_2016_Bacchiani_keynote.pdf)
3. Tara N. Sainath et al., "Multichannel Signal Processing with Deep Neural Networks for Automatic Speech Recognition." IEEE/ACM Transactions on Audio, Speech, and Language Processing (2017).
4. Zazo Candil, Rubén; Tara N. Sainath, Simko, Gabor; Parada, Carolina, Feature Learning with Raw-Waveform CLDNNs for Voice Activity Detection, InterSpeech 2016.
5. Sainath, Tara N., Oriol Vinyals, Andrew Senior, and Haşim Sak. "Convolutional, long short-term memory, fully connected deep neural networks.", ICASSP 2015.
6. Chan, William, Navdeep Jaitly, Quoc Le, and Oriol Vinyals. "Listen, attend and spell: A neural network for large vocabulary conversational speech recognition." In Acoustics, Speech and Signal Processing, ICASSP 2015.
7. Context dependent phone models for LSTM RNN acoustic modelling, ICASSP 2015.
8. Learning the Speech Front-end With Raw Waveform CLDNNs, InterSpeech 2015.

## Baidu

百度的DeepSpeech2的介绍：

（1）输入为频谱图；英文输出为{a, b, c, : : : , z, space, apostrophe, blank}，中文输出为｛包含罗马字母表，6000个汉字｝。

（2）采用BatchNorm(Batch Normalization) 方法，加速收敛；

（3）采用SortaGrid方法，保证CTC平稳性（短句优先训练）；

（4）采用GRU，GRU和LSTM的准确性相差不大，但GRU运算更快，；

（5）采用Lookahead Convolution和单向模型，因为双向LSTM的时延达不到要求。

- Deep Speech 2 End-to-End Speech Recognition in English and Mandarin, JMLR 2016.Gram-CTC: Automatic Unit Selection and Target Decomposition for Sequence Labelling, 2017.

## Amazon Alexa

Cocktail party problem

- Anchored Speech Detection, InterSpeech 2016.

## JHU

Dan Povey

1. Parallel training of DNNs with natural gradient and parameter averaging, ICLR Workshop 2015.
2. Ko, Tom, Vijayaditya Peddinti, Daniel Povey, and Sanjeev Khudanpur, "Audio augmentation for speech recognition.", InterSpeech 2015.

## CMU

1. EESEN: End-to-End Speech Recognition using Deep RNN Models and WFST-based Decoding, ASRU 2015.

# 相关研究

## [唤醒词检测](http://wiki.icenter.tsinghua.edu.cn/icenterwiki/index.php/唤醒词检测)

1. Michaely, Assaf Hurwitz, et al. "Keyword spotting for google assistant using contextual speech recognition." 2017 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU). IEEE, 2017.
2. Anchored Speech Detection, InterSpeech,2016
3. Convolutional Neural Networks for Small-footprint Keyword Spottin, InterSpeech, 2015
4. Small-footprint keyword spotting using deep neural networks, ICASSP, 2014

## 声音分离问题

声音分离问题：（separation） 音乐声源分离问题（Music source separation），采用深度卷积网络方法。

1. Deep Convolutional Neural Networks for Musical Source Separation. [MTG/DeepConvSep](https://github.com/MTG/DeepConvSep)
2. John R. Hershey, Zhuo Chen, Jonathan Le Roux, Shinji Watanabe, Yusuf Isik, “Deep clustering:Discriminative embeddings for segmentation and separation”, in Proc.ICASSP, Shanghai, April 2016.
3. Yusuf Isik, Jonathan Le Roux, Zhuo Chen, Shinji Watanabe, John R. Hershey, “Single-Channel Multi-Speaker Separation Using Deep Clustering”, in Proc. Interspeech, San Francisco, Sep 2016.
4. Yi Luo, Zhuo Chen, Jonathan Le Roux, John Hershey, Daniel P.W Ellis, ““Deep Clustering For Singing Voice Separation”, MIREX, task of Singing Voice Separation, 2016(1st and 2nd performance).

# 参考教材

1. 俞栋，邓力 著（俞凯， 钱彦旻 译），解析深度学习：语音识别实践，电子工业出版社，2016年7月.
2. 李航. 统计学习方法. 清华大学出版社, 北京, 2012.