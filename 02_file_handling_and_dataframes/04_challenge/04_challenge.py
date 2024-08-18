# ここにコードを書いてください
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加
iris_df['species'] = iris.target

# カスタムインデックスを設定 (例: ガクの長さと幅を組み合わせたインデックス)
iris_df.set_index(['sepal length (cm)', 'sepal width (cm)'], inplace=True)

# インデックスを確認
print(iris_df.head())

# インデックスをリセットしてから新しい列を追加
iris_df.reset_index(inplace=True)

# 新しい列を追加 (例: ガクの面積)
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']

# 新しい列を追加 (例: 花弁の面積)
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 変換後のデータを確認
print(iris_df.head())

# 品種ごとの平均値を計算
summary = iris_df.groupby('species').mean()

# 結果を表示
print(summary)

# 可視化の例
plt.scatter(iris_df['sepal_area'], iris_df['petal_area'], c=iris_df['species'])
plt.xlabel('Sepal Area')
plt.ylabel('Petal Area')
plt.title('Sepal Area vs Petal Area')
plt.show()