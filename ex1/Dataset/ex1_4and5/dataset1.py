import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def true_function(X):
    y = np.sin(np.pi * X * 0.8) * 10
    return y


np.random.seed(0)
xdot = np.random.uniform(-1, 1, size=20)
ydot = true_function(xdot)
df = pd.DataFrame({"観測点": xdot, "真値": ydot})
x = np.arange(-1, 1, 0.1)
y = true_function(x)

#ここからホワイトノイズ追加
ynoise = np.random.normal(loc=0, scale=np.sqrt(2), size=20)
whitenoise = ydot + ynoise/2
df = df.assign(観測値=whitenoise)#DataFrame型に観測値の列を追加

#plt.plot(x, y, label="true value")
#plt.scatter(xdot, ydot, c="magenta", label="observed dot")
#観測値は黒点
#plt.scatter(xdot, whitenoise, c="black", label="observed value")
#plt.legend()
#plt.show()
#fig = plt.figure()
#fig.savefig('./Dataset/ex1_3/1.3.png')

#TSV形式でファイル出力をする
df.to_csv('./Dataset/ex1_4and5/output.tsv', sep='\t', index=False)
#TSV形式からDataFrame型に変換する
df2 = pd.read_table('./Dataset/ex1_4and5/output.tsv', sep='\t')



