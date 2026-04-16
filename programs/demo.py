##import seaborn as sns
from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.widgets as wg

factorid=0
def changefactor(event):
    global factorid
    factorid+=1
    if factorid>=5:
        factorid = 0
    print(factorid)


#x = load_diabetes().data[:,2].reshape(-1,1)
factors=[load_diabetes().data[:,i].reshape(-1,1) for i in range(5)]
y = load_diabetes().target

models = [LinearRegression() for i in range(5)] # 線形回帰
##model = LinearRegression()
list(map(lambda mdl,x:mdl.fit(x,y),models,factors))
##model.fit(x, y) # BMI値から糖尿病の進行を予測する

fig, axis = plt.subplots(2,
                         gridspec_kw=dict(width_ratios=[1],height_ratios=[5,1]),
                         figsize=(8,5))

def setup():
    # ややこちらの方が慣れているためfigとaxisを使う

    # 式はグラフ中に描画するのでタイトルをシンプルに
    fig.suptitle('Linear Regression Analysis',fontsize = 15)

    btn=wg.Button(axis[1],"change factor")
    btn.on_clicked(changefactor)

    # 軸ラベル
    axis[0].set_xlabel("BMI(scaled)",fontsize = 12)
    axis[0].set_ylabel("Target",fontsize = 12)

    #(直線を描画すると描画範囲が変わったので手動で調整)
    axis[0].set_xlim(-0.18,0.21)
    axis[0].set_ylim(-50,410)

    #上と右の枠線を消す
    axis[0].spines["right"].set_visible(False)
    axis[0].spines[ "top" ].set_visible(False)



# 式をlatex形式にしてR^2値も追加
#txt_l = rf'$y = {model.coef_[0]:.1f} x + {model.intercept_:.1f}$'+"\n"+rf'$(R^2 = {model.score(x,y):.3f})$'
txt_l = rf'$y = {models[factorid].coef_[0]:.1f} x + {models[factorid].intercept_:.1f}$'+"\n"+rf'$(R^2 = {models[factorid].score(factors[factorid],y):.3f})$'

#散布図描画(重なっているところが多いので透明度も設定)
#axis[0].scatter(x,y,alpha=0.5,edgecolors="White")
axis[0].scatter(factors[factorid],y,alpha=0.5,edgecolors="White")

#回帰直線描画
#axis[0].axline(
#    (0,model.intercept_), (1,model.coef_[0]),
#    color = "darkred", linestyle = "--", label=txt_l
#    )# 散布図ではなく直線(破線)で表示
axis[0].axline(
    (0,models[factorid].intercept_), (1,models[factorid].coef_[0]),
    color = "darkred", linestyle = "--", label=txt_l
    )# 散布図ではなく直線(破線)で表示
##sns.regplot(x=x,y=y)


axis[0].legend(loc="upper left", borderaxespad=1)


plt.show()

######################################################################3

def main():
    is_drawing = False
    
    factors=[load_diabetes().data[:,i].reshape(-1,1) for i in range(5)]
    target = load_diabetes().target
    models = [LinearRegression() for i in range(5)] # 線形回帰
    list(map(lambda mdl,x:mdl.fit(x,target),models,factors))
    fig, axis = plt.subplots(
        2,
        gridspec_kw=dict(width_ratios=[1],height_ratios=[5,1]),
        figsize=(8,5)
    )
        
    fig.suptitle('Linear Regression Analysis',fontsize = 15)

    btn=wg.Button(axis[1],"change factor")
    btn.on_clicked(changefactor)

    # 軸ラベル
    axis[0].set_xlabel("Factor(scaled)",fontsize = 12)
    axis[0].set_ylabel("Target",fontsize = 12)

    #(直線を描画すると描画範囲が変わったので手動で調整)
    axis[0].set_xlim(-0.18,0.21)
    axis[0].set_ylim(-50,410)

    #上と右の枠線を消す
    axis[0].spines["right"].set_visible(False)
    axis[0].spines[ "top" ].set_visible(False)
    
    scat = axis[0].scatter(0,0,alpha=0.5,edgecolors="White")
    line = axis[0].axline((0,0),(0,0),color = "darkred", linestyle = "--", label="")
    legend = axis[0].legend(loc="upper left", borderaxespad=1)

    while is_drawing:
        scat.set_offsets(factors[factorid],y)
        line.set_data((0,models[factorid].intercept_), (1,models[factorid].coef_[0]))
        legend

if __name__ == "__main__":
    main()