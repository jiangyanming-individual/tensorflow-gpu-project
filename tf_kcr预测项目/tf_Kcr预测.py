# author:Lenovo
# datetime:2023/4/25 10:23
# software: PyCharm
# project:project_demo04


import tensorflow as tf
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")


import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

Amino_acid_sequence='ACDEFGHIKLMNPQRSTVWY'

word_to_id={
    'unk':0,'A':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'K':9,'L':10,
    'M':11,'N':12,'P':13,'Q':14,'R':15,'S':16,'T':17,'V':18,'W':19,'Y':20
}


train_filePath='./data/Kcr1_cv.csv'
test_filepath='./data/Kcr1_ind.csv'


def read_file(file_path):
    x_data=[]
    y_data=[]
    with open(file_path,mode='r',encoding='utf-8') as f:

        for line in f.readlines():
            one_data = []
            data,y_label=line.strip().split(',')
            # print(generate_data,y_label)
            for i in data:
                if word_to_id.get(i):
                    id=word_to_id[i]
                else:
                    id=0
                one_data.append(id)

            x_data.append(one_data)
            y_data.append(int(y_label))
            # print(x_data)

    return x_data,y_data
x_train,y_train=read_file(train_filePath)
x_test,y_test=read_file(test_filepath)

np.random.seed(20)
np.random.shuffle(x_train)
np.random.seed(20)
np.random.shuffle(y_train)
tf.set_random_seed(20)

np.random.seed(20)
np.random.shuffle(x_test)
np.random.seed(20)
np.random.shuffle(y_test)
tf.set_random_seed(20)


# x_train=np.reshape(x_train,(len(x_train),29))
x_train=np.array(x_train)
y_train=np.array(y_train)

x_test=np.array(x_test)
# x_test=np.reshape(x_test,(len(x_test),29))
y_test=np.array(y_train)

model=tf.keras.models.Sequential([
    tf.keras.layers.Embedding(21,10),
    tf.keras.layers.SimpleRNN(64,return_sequences=True),
    tf.keras.layers.SimpleRNN(32,return_sequences=True),
    tf.keras.layers.SimpleRNN(10),
    tf.keras.layers.Dense(2,activation="softmax")
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss_weights=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=tf.keras.metrics.sparse_categorical_accuracy
)

checkpoint_save_path='./checkpoint/kcr_predict.ckpt'

if os.path.exists(checkpoint_save_path+'.index'):
    print('----------------load the model--------------------')
    model.load_weights(checkpoint_save_path)

cp_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_save_path,
    save_weights_only=True,
    save_best_only=True,
    # monitor='loss' #因为没有测试集所以保存，只需要依靠loss
)

history=model.fit(x_train,y_train,batch_size=128,epochs=10,validation_data=(x_test,y_test),validation_freq=20,callbacks=[cp_callback])
model.summary()


loss=history.history['loss']
acc=history.history['sparse_categorical_accuracy']

val_loss=history.history['val_loss']
val_acc=history.history['val_sparse_categorical_accuracy'] #history中的准确率
# print(val_loss)

import matplotlib.pyplot as plt


plt.subplot(1,2,1)
plt.title("acc and test acc")
plt.plot(acc,label="Train acc")
plt.plot(val_acc,label="Test acc")
plt.xlabel("epoch")
plt.ylabel("generate_data")
plt.legend()


plt.subplot(1,2,2)
plt.title("loss and test loss")
plt.plot(loss,label="Train loss")
plt.plot(val_loss,label="Test loss")
plt.xlabel("epoch")
plt.ylabel("generate_data")
plt.legend()
plt.show()
