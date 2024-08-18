# ここにコードを書いてください
import pandas as pd
from sklearn import datasets

# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加
iris_df['species'] = iris.target

# データの概要を表示
print(iris_df.head())

# 欠損値の確認
print(iris_df.isnull().sum())

# 各列のデータ型を確認
print(iris_df.dtypes)

# 基本統計量を計算
stats = iris_df.describe().transpose()

# 統計情報を新しいDataFrameとして保存
stats_df = pd.DataFrame(stats, columns=['mean', '50%', 'std'])
stats_df.rename(columns={'50%': 'median'}, inplace=True)

# 統計情報をCSV形式で保存
stats_df.to_csv('iris_statistics.csv')

# 新しい特徴量を追加
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を算出
new_features_stats = iris_df[['sepal_area', 'petal_area']].describe().transpose()

# 統計情報のDataFrameに追加
stats_df = pd.concat([stats_df, new_features_stats[['mean', '50%', 'std']].rename(columns={'50%': 'median'})])
print(stats_df)

def filter_data(df, column, threshold):
    """
    指定した列の値がしきい値を下回る行を除外する
    """
    return df[df[column] >= threshold]

# 例: sepal_areaが15以上のデータをフィルタリング
filtered_df = filter_data(iris_df, 'sepal_area', 15)
print(filtered_df.head())

# DataFrameをCSV形式で保存
iris_df.to_csv('iris_with_features.csv', index=False)