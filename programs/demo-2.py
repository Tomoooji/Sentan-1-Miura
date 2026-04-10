#import tensorflow as tf
#from tensorflow import keras
#print(keras.__version__)
#"""
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets.mnist import load_data

# Cholet本の2章付属のコード
(train_images, train_labels), (test_images, test_labels) = load_data()
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255

model = Sequential([
Dense(128, activation="relu"),
Dense(10, activation="softmax")
]) # Kerasなら1行でニューラルネットワークのモデルを作成できる

model.compile(optimizer="rmsprop",
loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# ここがメインとなる訓練（若干時間がかかる）
model.fit(train_images, train_labels, epochs=3, batch_size=512*2)

model.evaluate(test_images, test_labels)
#"""