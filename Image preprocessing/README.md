对视网膜分支静脉阻塞眼底图像（BRVO）进行预处理

1.RGB_split.py对BRVO进行通道分离，把G通道的图像存为gchannel.npy

2.histogram_equali.py 全局和局部直方图均衡化，增强后的图像保存为loacl_histom.npy

3.FilpAndrotate.py 水平翻转和旋转

4.noise.py 添加椒盐噪声
