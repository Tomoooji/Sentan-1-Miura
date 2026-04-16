##import seaborn as sns
import numpy as np
from sklearn.datasets import load_diabetes # 使うライブラリをまとめて宣言しておく
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.widgets as wg

factor_name=[
    "Age","Sex","BMI","Blood Pressure","s1","s2","s3","s4","s5","s6"
]

factor_num = 10
factor_id = 2
txtfunc = ""

def changefactor(event):
    global factor_id
    factor_id+=1
    if factor_id>=factor_num:
        factor_id = 0

def main():
    is_drawing = True
    
    factors=[load_diabetes().data[:,i].reshape(-1,1) for i in range(factor_num)]
    target = load_diabetes().target
    models = [LinearRegression() for i in range(factor_num)] # 線形回帰
    list(map(lambda mdl,x:mdl.fit(x,target),models,factors))
    fig, axis = plt.subplots(
        2,
        gridspec_kw=dict(width_ratios=[1],height_ratios=[1,7]),
        figsize=(8,6)
    )
        
    #fig.suptitle('Linear Regression Analysis',fontsize = 15)
    axis[0].set_title('Linear Regression Analysis',fontsize = 15)

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
    
    
    while is_drawing:
        txtfunc=rf'$y = {models[factor_id].coef_[0]:.1f} x + {models[factor_id].intercept_:.1f}$'+"\n"+rf'$(R^2 = {models[factor_id].score(factors[factor_id],target):.3f})$'

        scat.set_offsets(list(zip(factors[factor_id],target.reshape(-1,1))))
        line.set_xy1((0,models[factor_id].intercept_))
        line.set_xy2((1,models[factor_id].coef_[0]))
        line.set_label(txtfunc)
        axis[1].legend(loc="upper left", borderaxespad=1)
        btn.label.set_text(f"change factor: {factor_name[factor_id]} -> {factor_name[0 if factor_id ==9 else factor_id+1]}")
        
        plt.pause(1)


if __name__ == "__main__":
    main()