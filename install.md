# scikit-learnのインストール方法
scikit-learnはPythonの機械学習ライブラリで分類・回帰・クラスタリング・次元削減・モデル選択・前処理などの機能が提供されている。scikit-learnのインストール方法はターミナルで下記のコマンドを打つ
```
$ python3 -m venv sklearn-env
$ source sklearn-env/bin/activate
$ pip3 install -U scikit-learn
```
仮想環境は必須ではないが、他のパッケージとの潜在的な競合を避けるために強く推奨する。
# librosaのインストール方法
音声認識や音声解析を行う場合には「**librosa**」というライブラリを使う。librosaのインストールは下記の通りにターミナルで実行する
pipの場合
```
$ pip install librosa
```

condaの場合
```
$ conda install -c conda-forge librosa
```
