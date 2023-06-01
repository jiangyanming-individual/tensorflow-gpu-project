# author:Lenovo
# datetime:2023/4/26 10:03
# software: PyCharm
# project:tensorflow-gpu项目

import tensorflow as tf

import tensorflow
print(tf.__version__)
print(tf.test.is_built_with_cuda()) # 判断CUDA是否可用
print(tf.test.is_gpu_available())  # 查看cuda、TensorFlow_GPU和cudnn

gpu_device=tf.test.gpu_device_name() #查看gpu的device
print(gpu_device)


#限制使用gpu:
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"  # =右边"0,1",代表使用标号为0,和1的GPU
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices()) #显示详细gpu信息；



#动态申请使用显卡

config=tf.ConfigProto()
config.gpu_options.allow_growth=True
session=tf.Session(config=config)

