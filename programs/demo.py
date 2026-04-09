##import numpy as np
#import seaborn as sns
from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = load_diabetes().data[:,2].reshape(-1,1) # 今回はライブラリに付属するデータを利用する
y = load_diabetes().target

model = LinearRegression() # 線形回帰を行う
model.fit(x, y) # BMI値から糖尿病の進行を予測する


# plt.scatter(x, y) # ナイーブなプロットはあまり美しいとは言えない
# plt.show()
"""
plt.figure(figsize=(6, 5)) # より美しいプロットを試みる
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red') # 回帰直線を赤線で加える
plt.xlabel('BMI'); plt.ylabel('Target') # x軸とy軸にラベルを加える
txt = f'Linear Regression: y = {model.coef_[0]:.1f} x + {model.intercept_:.1f}'
plt.title(txt) # 表題として回帰直線の数式を加える
plt.xlim(-0.2, 0.2)
"""

#sns.set_style("whitegrid")

# ややこちらの方が慣れているためfigとaxisを使う
fig, axis = plt.subplots()

#散布図描画(重なっているところが多いので透明度も設定)
axis.scatter(x,y,alpha=0.7)#

#axis.plot(x, model.predict(x),color = "black")
axis.axline((0,model.intercept_),(1,model.coef_[0]),
            color = "red",linestyle = "--")# 散布図ではなく直線(破線)で表示
#sns.regplot(x=x,y=y)

# 軸ラベル
axis.set_xlabel("Target")
axis.set_ylabel("BMI")

#(直線を描画すると描画範囲が変わったので手動で調整)
axis.set_xlim(-0.11,0.21)
axis.set_ylim(0,360)

# 式はグラフ中に描画するのでタイトルをシンプルに
txt_t = 'Linear Regression'
axis.set_title(txt_t)

# 式をlatex形式にしてR^2値も追加
formula_pos = [0.071,202]
txt_l = rf'$y = {model.coef_[0]:.1f} x + {model.intercept_:.1f}  (R^2 = {model.score(x,y):.3f})$'
axis.text(formula_pos[0],formula_pos[1],txt_l)


plt.show()