from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = load_diabetes().data[:,2].reshape(-1,1) # 今回はライブラリに付属するデータを利用する
y = load_diabetes().target

model = LinearRegression() # 線形回帰を行う
model.fit(x, y) # BMI値から糖尿病の進行を予測する


# plt.scatter(x, y) # ナイーブなプロットはあまり美しいとは言えない
# plt.show()

plt.figure(figsize=(6, 5)) # より美しいプロットを試みる
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red') # 回帰直線を赤線で加える
plt.xlabel('BMI'); plt.ylabel('Target') # x軸とy軸にラベルを加える
txt = f'Linear Regression: y = {model.coef_[0]:.1f} x + {model.intercept_:.1f}'
plt.title(txt) # 表題として回帰直線の数式を加える
plt.show()