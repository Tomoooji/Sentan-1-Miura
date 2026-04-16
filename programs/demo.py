##import seaborn as sns
from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = load_diabetes().data[:,2].reshape(-1,1) # 今回はライブラリに付属するデータを利用する
y = load_diabetes().target

model = LinearRegression() # 線形回帰を行う
model.fit(x, y) # BMI値から糖尿病の進行を予測する

##sns.set_style("whitegrid")

# ややこちらの方が慣れているためfigとaxisを使う
fig, axis = plt.subplots(figsize=(8,5))

# 式はグラフ中に描画するのでタイトルをシンプルに
txt_t = 'Linear Regression Analysis'
axis.set_title(txt_t,fontsize = 15)

# 軸ラベル
axis.set_xlabel("BMI(scaled)",fontsize = 12)
axis.set_ylabel("Target",fontsize = 12)

#(直線を描画すると描画範囲が変わったので手動で調整)
axis.set_xlim(-0.18,0.21)
axis.set_ylim(-50,410)

# 式をlatex形式にしてR^2値も追加
##formula_pos = [0.11,190]
txt_l = rf'$y = {model.coef_[0]:.1f} x + {model.intercept_:.1f}$'+"\n"+rf'$(R^2 = {model.score(x,y):.3f})$'
#axis.text(formula_pos[0],formula_pos[1],txt_l)

#上と右の枠線を消す
axis.spines["right"].set_visible(False)
axis.spines[ "top" ].set_visible(False)

#散布図描画(重なっているところが多いので透明度も設定)
axis.scatter(x,y,alpha=0.5,edgecolors="White")

#回帰直線描画
#axis.plot(x, model.predict(x),color = "black")
axis.axline((0,model.intercept_),
            (1,model.coef_[0]),
            color = "darkred",
            linestyle = "--",
            label=txt_l
            )# 散布図ではなく直線(破線)で表示
##sns.regplot(x=x,y=y)

axis.legend(loc="upper left", borderaxespad=1)

plt.show()