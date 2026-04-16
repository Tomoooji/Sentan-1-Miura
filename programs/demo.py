"""
## 注意 ## 
juypter notebookで実行するとグラフ上のボタンを押せないようなので
matplotlibのグラフがウィンドウででる環境で実行した方が良いと思われます
"""

##import seaborn as sns
import numpy as np
from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.widgets as wg

# 説明変数の名前たち
factor_name=[
    "Age","Sex","BMI","Blood Pressure","s1","s2","s3","s4","s5","s6"
]

# 説明変数の切り替え用
factor_num = 10
factor_id = 2
txtfunc = ""

# ボタンを押したときに説明変数を切り替える関数
def changefactor(event):
    global factor_id
    factor_id+=1
    if factor_id>=factor_num:
        factor_id = 0


def main():
    is_drawing = True
    # 説明変数ごとに線形回帰モデルを作成
    factors=[load_diabetes().data[:,i].reshape(-1,1) for i in range(factor_num)] # 説明変数
    target = load_diabetes().target # 目的変数
    models = [LinearRegression() for i in range(factor_num)] # 線形回帰モデル
    list(map(lambda mdl,x:mdl.fit(x,target),models,factors)) # 線形回帰

    # グラフ画面の作成
    fig, axis = plt.subplots(
        2,
        gridspec_kw=dict(width_ratios=[1],height_ratios=[1,7]),
        figsize=(8,6)
    )
    
    # グラフのタイトル(上の方が概念的にはきれいだが下の方が余白が良い感じなのでそっちを使う)   
    #fig.suptitle('Linear Regression Analysis',fontsize = 15)
    axis[0].set_title('Linear Regression Analysis',fontsize = 15)

    # 説明変数を切り替えるボタン
    btn=wg.Button(axis[0],"")
    btn.label.set_fontsize(12)
    btn.on_clicked(changefactor)

    # 軸ラベル
    axis[1].set_xlabel("Factor(scaled)",fontsize = 12)
    axis[1].set_ylabel("Target",fontsize = 12)

    #(直線を描画すると描画範囲が変わったので手動で調整)
    axis[1].set_xlim(-0.18,0.21)
    axis[1].set_ylim(-50,410)

    #上と右の枠線を消す
    axis[1].spines["right"].set_visible(False)
    axis[1].spines[ "top" ].set_visible(False)
    
    #先に型枠だけ作っとく
    scat = axis[1].scatter([],[],alpha=0.5,edgecolors="White")
    line = axis[1].axline((0,0),(1,0),color = "darkred", linestyle = "--")
    #axis[0].legend(loc="upper left", borderaxespad=1)
    
    
    # ボタンが押された時にグラフ上の要素を更新できるようにしている
    while is_drawing:
        # 凡例に出す数式の更新
        txtfunc=rf'$y = {models[factor_id].coef_[0]:.1f} x + {models[factor_id].intercept_:.1f}$'+"\n"+rf'$(R^2 = {models[factor_id].score(factors[factor_id],target):.3f})$'

        # 散布図と回帰直線の更新
        scat.set_offsets(list(zip(factors[factor_id],target.reshape(-1,1))))
        line.set_xy1((0,models[factor_id].intercept_))
        line.set_xy2((1,models[factor_id].coef_[0]))
        line.set_label(txtfunc)
        
        # 凡例の更新
        axis[1].legend(loc="upper left", borderaxespad=1)
        
        # ボタンの文字の更新
        btn.label.set_text(f"change factor: {factor_name[factor_id]} -> {factor_name[0 if factor_id ==9 else factor_id+1]}")
        
        # 画面全体の再表示(1秒毎)
        plt.pause(1)

if __name__ == "__main__":
    main()