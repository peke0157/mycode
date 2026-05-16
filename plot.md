# FFT前のグラフ
今回は以下のファイル。ディレクトリ構成を例としている
```
ongakukaiseki
├──python
│  └──exp
│     │  
│     ├─blues 
│     │  ├─blues.00000.wav
│     │  ├─blues.00001.wav
│     │  ├─blues.00002.wav  
│     │  │          ⋮
│     │  └─blues.00099.wav  
│     │  
|     ├──classical
|     |  ├──classical.00000.wav
|     |  ├──classical.00001.wav
|     |  ├──classical.00002.wav 
│     │  │          ⋮
|     |  └──classical.00099.wav 
│     │  
|     ├─country 
│     │  ├─country.00000.wav
│     │  ├─country.00001.wav
│     │  ├─country.00002.wav
│     │  │          ⋮
│     │  └─country.00099.wav
│     |
|     ├─disco
│     |  ├─disco.00000.wav
│     |  ├─disco.00001.wav
│     |  ├─disco.00002.wav
│     │  │          ⋮
│     |  └─disco.00099.wav
│     |
|     ├──environment
│     |  ├──5-9032-A-0.wav  
│     |  ├──5-51149-A-25.wav
│     |  ├──5-61635-A-8.wav
│     │  │          ⋮
│     |  └──5-263902-A-36.wav  
│     |
|     ├──hiphop
|     │  ├──hiphop.00000.wav
|     │  ├──hiphop.00001.wav
|     │  ├──hiphop.00002.wav    
│     │  │          ⋮
|     │  └──hiphop.00099.wav    
│     |
|     ├─jazz  
│     |  ├─jazz.00000.wav
│     |  ├─jazz.00001.wav
│     |  ├─jazz.00002.wav
│     │  │          ⋮
│     |  └─jazz.00099.wav
│     |
|     ├─metal  
│     |  ├─metal.00000.wav
│     |  ├─metal.00001.wav
│     |  ├─metal.00002.wav
│     │  │          ⋮
│     |  └─metal.00099.wav
│     |
|     ├─pop  
│     |  ├─pop.00000.wav
│     |  ├─pop.00001.wav
│     |  ├─pop.00002.wav
│     │  │          ⋮
│     |  └─pop.00099.wav
│     |
|     ├─reggae  
│     |  ├─reggae.00000.wav
│     |  ├─reggae.00001.wav
│     |  ├─reggae.00002.wav
│     │  │          ⋮
│     |  └─reggae.00099.wav
│     |
|     ├─rock  
│     |  ├─rock.00000.wav
│     |  ├─rock.00001.wav
│     |  ├─rock.00002.wav
│     │  │          ⋮
│     |  └─rock.00099.wav
|
└──plot.ipynb etc.
```
必要モジュールをインポートする
```
import numpy as np
import matplotlib.pyplot as plt
import librosa
from pathlib import Path
```
以下のコード
```
base_dir = Path('test')
for audio_dir in base_dir.glob('*.wav'):
    y, sr = librosa.load(audio_dir)

    L = len(y)
    t = np.arange(0,L) / sr
    
    

    plt.plot(t,y)
    plt.title('Audio waveform')
    plt.xlabel('time(s)')
    plt.ylabel('Amplitude')

    plt.show()
```
**Pathlib**のライブラリを使うことでファイル・ディレクトリのパスをオブジェクトとして操作・処理することができる。「base_dir = Path('test')」これはtestディレクトリのパスを設定することでtestディレクトリの中にあるファイルを操作することができる。for文で「test」ディレクトリにある音声ファイルの個数分音声波形を出力している。

# MFCC適用のグラフをプロットするコード
音声・音楽ファイルを機械学習で扱うにはmfccを適用して特徴量を抽出する。**MFCC（メル周波数ケプストラム係数）**とは、音声認識や音声処理において最も広く使用されている特徴量の一つ。MFCCは、音声信号を周波数領域で分析し、人間の耳が音を知覚する方法に近い形で特徴を抽出することを目的としている。これにより、音声認識システムは単なる音の強度やピッチの違いではなく、人間の聴覚の特性を考慮した音声データのパターンを理解することができる。
MFCCのメリットとして、聴覚特性を反映した特徴を抽出することができる点である。単純な周波数分析では、高周波数成分が重要視されすぎることがあるが、MFCCではメルスケールを使用することで、低周波数と高周波数のバランスを適切に調整することができる。
- MFCCを適用したソースコードは[plot.ipynb](https://github.com/peke0157/ongakukaiseki/blob/main/python/plot.ipynb)の最終セルで提示している。

- save_dirで抽出した学習済みモデルの保存先ディレクトリを「expdata」にしている。librosaライブラリはmfccするときも便利で、librosaを用いることでmfccの計算が一行で行うことができる。
### 使い方
```
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

```
- 今回使っているパラメータ
 - y: 音声時系列データ。マルチチャンネルに対応
 - sr:番号 > 0 （スカラー） 
 サンプリングレート
 - n_mfcc: int > 0
 返却するMFCCの数

librosa.display.specshow()はスペクトログラム/クロマグラム/cqtなどを表示するための関数である。これもlibrosaライブラリにあるので、スペクトログラムの表示が簡単にできる。