# Pythonチートシート

メソッドなどの使い方など。書いたことあるメソッドは出来るだけ頭の片隅に残しておきたい。。。

## 標準機能

### 型を調べる

- type(調べたいオブジェクト)
- **.dtypes** : それぞれのカラムの型を調べる

### 配列

	[] : 配列
	l = list()

#### スライス

	l[:-1] : 一番最後の1つ前の要素まで

#### 追加(list型)

	squares = []
	squares.append( x )

### 辞書, リスト

- **{}** : 辞書型
- d = dict()

辞書型の値取得はgetメソッドを使うが良し。

	d.get('key2') # キーが存在しない時は「NoneType」が返る
	d.get('key1', 'NO KEY') # 「NoneType」の代わりに独自に指定も出来る


### リスト内表記

	squeres = [x ** 2 for x in range(10)]

#### 要素の数

	len()

### range

	range(end)          # 0 ~ endの前まで
	range(start, end)
	range(start, end, distance)

### ループ

	for k in dictional:  # 辞書型の時はkにはキーが入る
	for k, v in dict.items(): # dictionary型の時使う？
	for x, i in enumerate(x_list): # インデックス付きループ x: value, i: 何番目か
	for x, y in zip(x_list, y_list): # 同時に取り出せる

#### zip()

forループの中で、**複数のリストの要素を同時に**取得

	for score, name in sorted(zip(scores, names), reverse=True):
		print('{}: {}'.format(score, name)

#### 他メソッド

	'-'.join(配列)  # 配列を'-'で繋ぐ
	re.split('（|）', text)  # textを「（」や「）」で分割
	re.sub(r"\D", "", text)  # 数値(文字列返却)のみにする
### 高階関数

引数か戻り値に関数が指定されている関数  
**lambda式**で使っているアレ

- map()  # 繰り返し可能なオブジェクトの、全ての要素にある処理をするためのもの
- filter()  # 繰り返し可能なオブジェクトに対して、ある条件がTrueになる要素だけにフィルタリングするためのもの
  - df.filter(like='芝・ダ', axis=1) # 行名・列名を部分一致で指定
- reduce()  # 繰り返し可能なオブジェクトに対して、累積的な処理をして**値**を1つにまとめる   

データの部分一致で指定(正規表現)

	df['gender'].str.match('male')
	df['name'].str.match('.*a.*')

	^ 先頭, $ 末尾, * 任意

## Pandas(DataFrame, Series)

### 初期化

- df = pd.DataFrame()
- df = pd.DataFrame(s) # s:Series型。Series型をDataFrame型へ変換する

### データを調査する

- .head()
- .tail()
- .info()
- .describe()
- .columns
- .index
	- .index.unique()
- .shape ＃行数・列数の確認
- .reshape()  # 次元の形を変える
- .nunique() # それぞれのカラムのユニークなデータの数
- .value_counts()
	- .value_counts().sort_index() # indexでソート
	- .value_counts().sort_values() # 値でソート
	- .value_counts().sort_values(ascending=False) # 降順
- .dtypes # 型の確認
	- .dtypes.value_counts()
- .corr() # 相関係数を算出
- .rolling() # 移動平均、時系列データでよく用いる
- .mode() # 最頻値
- .mean()  # 平均
- .std()  # 標準偏差
- .cumsum() # 累積和
- .expanding()
	- .expanding().mean()  # 先頭から順に平均を計算していく
	- .expanding().agg(['カラム名1', 'カラム名2'])
- .isin(['']) dfで指定したカラムに、isin()で指定した値が入っているかどうか。boolを返す
- .cut()  # ビニングなどで使う

### 条件によるデータの抽出

- df > 0
- df[df>0]
- df[df['C']>0]
- df['XX'].where(条件, v) # 'XX'のカラムを、条件に合う**以外**の値がvに変更される
- df['XX'].mask()       # whereの逆
- df.loc[0:10, ['col1', col2']] # 行と列の範囲を指定して取得
- df.query() # 複数条件の指定で、特定カラムだけ出力
	- df.query('カラム名==1')
- df.where(条件, 正の時の値, 負の時の値) 条件によって値を設定する

### データの整形
- .set_index() # indexの設定
- .rename() # カラム名を変更
- .resample()
  - アップサンプリング(間のデータの補完)
  - ダウンサンプリング
- .map()  Seriesのみ、辞書OK, リストOK
- .apply() Siries以外もOK, mapダメ、listダメ
- .apply(lambda ○:○*2) 
- .str.extract(正規表現とか) # 抽出（r'(\D+)'） +を付けると固まりを抽出
- .duplicated() # 重複行を削除
- .shift() # データをずらす。行方向、列方向、ずらす幅など指定
- .argmax( , axis=1) # 行単位で一番大きい配列の位置を返す 
- .replace('置換する文字列', '置換後文字列', inplace=True) 文字列の置換
  - df.replace('CA', 'California', inplace=True)
- .clip()  1 ~ 99%の中にデータを入れる, 上限や下限を設定し、超えた場合はその制限値に変換する


### df.groupby()

- .groupby(['', '', '', ''])[['', '']].mean()
- .groups # グルーピングの内訳を見る
	- .groups.keys()
- .agg()
	- .agg(lambda x: print(x))
- .size() # key別のサイズ
- .sum()
- .get_group('グループ名')

#### Loop

	for key, group in groups:
    	print(key, group)

### Pivot Table

	pd.pivot_table(msales, index='staff', columns='year', values='amount', aggfunc='sum').reset_index()

### ビニング

- df.cut() と .plot.bar()を組み合わせたりして使う

### 日時

	.to_datetime()  # 文字列をdatetime64型に変換
	pd.to_datetime('2021-06-21')
	pd.to_datetime(xxx['日付'], infer_datetime_format=True)
	pd['Date'].dt.weekday # 曜日情報を取得
	datetime.strptime(str(221119, '%Y%m%d')

#### Serise

- df['xxx'].iloc[-1] # 1つの値を取り出す。"最後の1行を取り出す"というメソッドの呼び方

### 集計
- .agg() # 一度に複数の処理を適用できる。groupby()の後に使うこと多し
- .crosstab(df, df, margins=True) # クロス集計（カテゴリごとの出現回数・頻度を算出）
- pd.cut(), .qcut() # クロス集計するためにも必要。ビニング（数値データを例えば0< <10, 10<= <20,とか）。.qcutは量を区切る。
- .diff()
- .rolling()
- .pct_change()


### 外れ値を削除

#### 数値の大きい上位2位のデータを表示

- data.sort_values(by = 'GrLivArea', ascending = False)[:2]

ascending=False は'GrLivArea'の高いデータから順に並べ替えられる

#### 判明したデータのIdの値を指定して削除

- data.drop(index = data[data['Id'] == 1299].index)
- data.drop(index = data[data['Id'] == 524].index)

#### 欠損値を除外（削除）

- df.dropna(how='all').dropna(how='all', axis=1)

how='any'がデフォルト値で、欠損値が１つでも含まれていれば、その行が削除される。

#### 欠損値を置換（穴埋め）

- .fillna() # 別の値で埋める
- df_train.fillna({'確定着順': 10})
- .fillall()
- .dropna()
- .replace()
- .mask()
- .drop() # カラムを削除する
  - .drop(['', ''], axis=1, inplace=True)
- df[df['人気'].isnull()] # 欠損値があるデータを取り出す


#### 欠損値を抽出
- .isnull()
- .isnull().sum() # 欠損値の数
- df.isnull().sum()[df.isnull().sum() > 0] # ヌル値があるデータだけを表示
- .any()
- df.isnull().any()

### 結合(DataFrame - DataFrame)

#### join

**デフォルトはouter join** 
indexで結合する。  
**横**結合で使うと良い。  
インデックスで結合できないとき、mergeを使う。

#### merge

**デフォルトはinnner join** 
**横**結合で使うと良い。  
pd.merge(df1, df_rejs, left_on='騎手コード', right_on='コード', how='left')
- left_on 左のデータフレームの結合キー
- right_on 右のデータフレームの結合キー
- how どちら側をベースにするかの指定

#### concat

**縦**結合で使うと良い。  
デフォルトで文字コードでソートされる。回避するには(how='left')  
基本は縦列の結合に使いがち。横に結合したい時はaxis=1を指定  
**元データは更新されない。**

データフレームのリストを作ってからpd.concat()で縦に結合するのが便利そう。

	pd.concat([df1, df2, df3])

#### デザインパターン(DataFrame - Serise)

	def some_func(data):
	    ODDS = 80.0
	    shiji = np.round(ODDS / data.values, 2) # numpyで計算
	    return pd.Serise(shiji, index=shiji.index, name='何かの名前') # numpy -> Seriseへ変換
	    											　　　　　　　　# indexとnameを指定する
	odds_s = some_func(org_df['odds'])
	org_df = org.df.join(odds_s) # DataFrameとSeriseの結合


### ダミー変数化

- pd.get_dummies()

### 関数の適用
.apply()

### 型変換

.astype()
**result_csv['月'].astype(str).str.zfill(2)** : strにキャストしてstr型のオブジェクトを取得してから、zfillでゼロ埋めする

### CSV

	pd.read_csv('xxx.csv')
	to_csv('xxx.csv', header=True, index=False)

### ループ

#### Series

- __iter__() # valueのみをイテレーション
- iteritems() # indexとvalueをイテレーション

#### DataFrame

- __iter__() # columnsのみをイテレーション
- iteritems() # **列**単位でイテレーション
- iterrows() # **行**単位でイテレーション
- itertuples() # 行データがtupleで返ってくる。こちらの方が高速らしい

#### DataFrame

- for i, v in df.iterrows(): # indexとデータ(v)を同時に取得。vはSeries型
- for tpl in df.itertuples(): # １行ずつをタプルで取得
- for i in df[''].unique(): # ユニークな値だけを繰り返す
- for name, group in class_groupby:  # name: グループ名、group: グループの中身

## Numpy

- np.sum(list) # 要素の和を求める
- np.cumsum() # 配列を順に足した和を求める
- np.searchsorted(list, num) # リストに値を挿入する際のインデックスを返す
- np.asarray() # 元のNumpy配列と同期され続けるコピーを作る場合
- np.asfarray  # 配列内の文字列を数値に変換する
- np.array # Numpy配列のコピーを作る
- df['xxx'] = np.ndarray型
- np.where(pred<0.5, 0, 1)  # 2項演算子みたいなもの？

### DataFrame <-> Numpy

- df.to_numpy() # DataFrameをNumpyに変換する

### フロー的な感じ

total_pre = np.empty((0, 7), int) 
total_pre = np.vstack([total_pre, [race_index, a, b, c, d, e, f]])


## 機械学習など

## SciPy

- sp.stats.zscore(データ, axis=1) # データの標準化

## LabelEncorderの使い方

	import seaborn as sns
	import pandas as pd
	from sklearn import preprocessing
	
	titanic = sns.load_dataset("titanic")
	for column in ['sex', 'class']:
	    #print(titanic[column].shape)
	    le = preprocessing.LabelEncoder()
	    le.fit(titanic[column])
	    titanic[column] = le.transform(titanic[column])
	    
	titanic

### 一遍にやりたい時は**fit_transform()**もある

### pandasのカテゴリー変数

	for column in ['sex', 'class']:
	    titanic[column] = df2[column].astype('category')

### 切片や傾き
	model.coef_
	model.intercept_

## グラフを書く(Seaborn)

	import seaborn as sns

### 相関図
	corr = df_titanic.corr()
	mask = np.triu(np.ones_like(corr, dtype=bool))
	f, ax = plt.subplots(figsize=(11,9))
	cmap = sns.diverging_palette(230, 20, as_cmap=True)
	sns.heatmap(corr, cmap=cmap, mask=mask, vmax=.3, center=0, annot=True, square=True, linewidth=.5, cbar_kws={"shrink":.5}, annot_kws={"size":10})

### 箱ひげ図
#### その1
	sns.set(font_scale=2)
	plt.figure(figsize=(10,5))
	ax = sns.boxplot(x='Age', orient='h', data=df_titanic, fliersize=8)
#### その2
	sns.set(font_scale=2)
	plt.figure(figsize=(10,5))
	ax = sns.boxplot(x='Age', y='Survived', orient='h', data=df_titanic, fliersize=8)

### 棒グラフ
	ax = sns.barplot(x='Sex', y='Survived', data=df_titanic)
	ax = sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df_titanic)

### 複合グラフ
	sns.set(font_scale=2)
	plt.figure(figsize=(12,8))
	sns.distplot(df_titanic[df_titanic['Survived']==0]['Age'], color='red', label='0')
	sns.distplot(df_titanic[df_titanic['Survived']==1]['Age'], color='skyblue', label='1')
	plt.legend()

### Udemy
	ax = sns.countplot('Sex', data=df_titanic)
	ax = sns.countplot('Sex', data=df_titanic, hue="Pclass") # 相関を足す
	
	def male_female_child(passenger):
	    age, sex = passenger
	    if age < 16:
	        return 'child'
	    else:
	        return sex
	    
	df_titanic['person'] = df_titanic[['Age', 'Sex']].apply(male_female_child, axis=1)
	
	df_titanic['Age'].hist(bins=70) # ヒストグラム

#### カーネル密度推定
	fig = sns.FacetGrid(df_titanic, hue='Sex', aspect=4)
	fig.map(sns.kdeplot, 'Age', shade=True)
	oldset = df_titanic['Age'].max()
	fig.set(xlim=(0,oldset))
	fig.add_legend()
	
	sns.countplot('Cabin', data=cabin_df, palette='winter_d', order=sorted(set(cabin_df.Cabin))) # ソートして表示
	
	from collections import Counter

#### データにNaNがあるかないかを調べる
	Counter(df_titanic.Embarked)
	df_titanic.Embarked.value_counts()
	
	sns.factorplot('Pclass', 'Survived', data=df_titanic, order=[1,2,3])
	sns.lmplot('Age', 'Survived', hue='Pclass', data=df_titanic, palette='winter', hue_order=[1,2,3])
	sns.lmplot('Age', 'Survived', hue='Sex', data=df_titanic, palette='winter', x_bins=generations)
	generations = [10,20,40, 60, 80]
	sns.lmplot('Age', 'Survived', hue='Pclass', data=df_titanic, palette='winter', hue_order=[1,2,3], x_bins=generations)


### KeyError

	try:
	    data['a':'b']
	except KeyError as e:
	    print(type(e))
	    print(e)
    
## ユニットテスト

- Pytest  ライブラリ
- pytest-asyncio  非同期処理用

## コードプレビュー

- flake8

## CI/CDの準備

	$ pip freeze > requirements.txt


## デザインパターン

### 配列の中で関数を使ったり、引数2つだったり
	def male_female_child(passenger):
	    age, sex = passenger
	    if age < 16:
	        return 'child'
	    else:
	        return sex
	    
	df_titanic['person'] = df_titanic[['Age', 'Sex']].apply(male_female_child, axis=1)

### コールバック関数

**関数名に()を付けない**ことで**関数ポインタ**になる。  

コールバック関数を呼び出す関数を定義

	def handler(func, *args):
	    return func(*args)
		
コールバック関数を定義

	def say_hello(name):
	    print("Hello.", name)
	    
実行

	if __name__ == "__main__":
	    callback = say_hello
	    handler(callback, 'to_letter')
