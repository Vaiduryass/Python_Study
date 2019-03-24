import tensorflow as tf
from tensorflow.python.platform import gfile
import INCEPTION_V3_demo
import os.path
import  random
import numpy as np
import glob

BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'

#图像输入张量所对应的名称。
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'

#下载的谷歌训练好的Inception-v3模型文件目录。


MODEL_FILE = 'graph.pb'



def create_image_test_lists():
    INPUT_DATA = 'test'
    file_list = []
    extensions = ['jpg', 'jpeg', '#JPG', '#JPEG']
    for extension in extensions:
        file_glob = os.path.join(INPUT_DATA, '*.' + extension)
        file_list.extend(glob.glob(file_glob))
    return file_list 

image_path = create_image_test_lists()[0]
#获取图片内容。
image_data = gfile.GFile(image_path, 'rb').read()

def get_bottleneck_values():
    #load graph
    with gfile.GFile("path/to/model/classify_image_graph_def.pb",'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    #加载读取的Inception-v3模型，并返回数据输入所对应的张量以及计算瓶颈层结果所对应
    #的张量。
    bottleneck_tensor, jpeg_data_tensor = tf.import_graph_def(graph_def,
    return_elements=[BOTTLENECK_TENSOR_NAME, JPEG_DATA_TENSOR_NAME])

    with tf.Session() as sess:
        bottleneck_values = sess.run(bottleneck_tensor, {jpeg_data_tensor: image_data})
        bottleneck_values = np.squeeze(bottleneck_values)

    return bottleneck_values
    
def main(self):
    train_bottlenecks = get_bottleneck_values()
    #load graph
    saver = tf.train.import_meta_graph("path/to/save/model.ckpt.meta")

    with tf.Session() as sess:
        saver.restore(sess, "path/to/save/model.ckpt")
        train_bottlenecks = np.reshape(train_bottlenecks, (1,2048))
        
        c1 = sess.run("final_training_ops/Softmax:0",feed_dict={"BottleneckInputPlaceholder:0":train_bottlenecks})
        print(c1)
        

if __name__ == '__main__':
    tf.app.run()

