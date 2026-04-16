from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.datasets.mnist import load_data

#setting
batch_size = 512*2
epochs = 25#20#15#10#3

#+epoch=10: accuracy: 0.9660 - loss: 0.1125
#+epoch=15: accuracy: 0.9706 - loss: 0.0976   
#+epoch=20: accuracy: 0.9737 - loss: 0.0875
#optimaizer=adam: accuracy: 0.9747 - loss: 0.0855
#+epoch=25: accuracy: 0.9757 - loss: 0.0783
#+learning_rate=0.01: accuracy: 0.9791 - loss: 0.0968
#+learning_rate=0.005: accuracy: 0.9789 - loss: 0.0871 
#+learning_rate=0.002: accuracy: 0.9772 - loss: 0.0761
#+Dropout(0.2): accuracy: 0.9784 - loss: 0.0703
#こぴぺ:accuracy: 0.9915 - loss: 0.0269
#+Dropout(0.5): accuracy: 0.9931 - loss: 0.0215
#rate0.5->0.2: accuracy: 0.9935 - loss: 0.0208 

#2次元で扱う
(train_images, train_labels), (test_images, test_labels) = load_data()
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
# ピクセルの値を 0~1 の間に正規化
train_images, test_images = train_images / 255.0, test_images / 255.0

#作ってからaddしていく
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

#あだむ
model.compile(
    optimizer= "adam",#keras.optimizers.Adam(learning_rate=0.002),#"rmsprop",
    loss="sparse_categorical_crossentropy", 
    metrics=["accuracy"]
)

#パラメータは上のほうに移動
model.fit(
    train_images,
    train_labels,
    epochs=epochs,
    batch_size=batch_size,
)

model.evaluate(test_images, test_labels)
#lossが低く、accuracyが高いほど良いモデル
