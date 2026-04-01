import gradio as gr
import numpy as np
import joblib
import librosa


# 予測関数
def predict(text):
    y, sr = librosa.load('*.wav')
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    # 2次元配列を変更する処理
    mean = np.mean(mfccs, axis=1)
    std = np.std(mfccs, axis=1)
    concatenate = np.concatenate([mean, std])
    
    
    # 学習モデルの反映
    scaler = joblib.load('expscaler.pkl')
    model = joblib.load('expmodel.pkl')

    return genru


# Grインターフェイスの作成
demo = gr.Interface{
    fn=predict,
    inputs=gr.Audio(type='filepath')
    outputs=
    title="音楽ジャンル測定アプリ"
}

# アプリケーションの気道
if __name__ == "__main__":
    demo.launch()