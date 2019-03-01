import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#加载mnist_inference.py和mnist_train.py中定义的常量和函数。
import mnist_inference
import mnist_train

#每10秒加载一次最新的模型，并在测试数据上测试最新模型的正确率。
EVAL_INTERVAL_SECS = 10

def evaluate(mnist):
    with tf.Graph().as_default() as g:
        #定义输入输出的格式。
        x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}

        #直接通过调用封装好的函数来计算前向传播的结果。因为测试时不关注正则化损失的值，
        y = mnist_inference.inference(x, None)

        #使用前向传播的结果计算正确率。如果需要对未知的样例进行分类，那么使用
        #tf.argmax(y, 1)就可以得到输入样例的预测类别了。
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        #通过变量重命名的方式来加载模型，这样前向传播的过程中就不需要调用滑动平均
        #的函数来获取平均值了。这样就可以完全共用mnist_infeence.py中的定义的
        #前向传播过程。
        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variable_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variable_to_restore)

        #每隔EVAL_INTERVAL_SECS秒调用一次计算正确率的过程以检测训练过程中正确率的变化
        while True:
            with tf.Session() as sess:
                #tf.train.get_chepoint_state函数会通过chekpoint文件自动
                #找到目录中最新模型的文件名。
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    #加载模型。
                    saver.restore(sess, ckpt.model_checkpoint_path)
                #通过文件名取得模型保存时迭代的轮数。
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                print("After %s training steps(s), validation accuracy= %g" % (global_step, accuracy_score))
        else:
            print('No chekpoint file found')
    return time.sleep(EVAL_INTERVAL_SECS)

def main(argv=None):
    mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
    evaluate(mnist)

if __name__ == '__main__':
    tf.app.run()


