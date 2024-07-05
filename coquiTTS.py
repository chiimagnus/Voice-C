from llama_cpp import Llama
import whisper
import sounddevice as sd
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
from datetime import datetime
import os
from TTS.api import TTS

# 创建 responses 文件夹（如果不存在）
responses_dir = "responses"
os.makedirs(responses_dir, exist_ok=True)

# 加载Coqui TTS模型
tts_model = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False, gpu=False)

# Coqui TTS播放回复文本
def text_to_speech(text, wav_response_path):
    try:
        # 使用Coqui TTS生成语音
        tts_model.tts_to_file(text=text, file_path=wav_response_path)
        
        # 播放音频
        fs, data = wavfile.read(wav_response_path)
        sd.play(data, fs)
        sd.wait()

        print(f"Response played and saved to {wav_response_path}.")
    except Exception as e:
        print(f"Error in text_to_speech: {e}")

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 获取当前时间戳并格式化为字符串

    # AI回复-文本形式
    response = "早八我没去，张仕杰起来上了个厕所就赶紧去了，很麻利这次，因为快迟到了，签到交作业事第一大事。我没睡好太困了，于是临时请求张仕杰帮我交作业和签到。我就在想一个事情，一到关键时候，还是得靠身边人，所以平常我就得让身边人信任我，我是靠得住的，这样关键的时候肯定会有人伸出援助之手。张仕杰二话不说就答应了我交作业和签到，之前的话他可能是“你不想去，我也不想去，你去吧，你帮我签一个吧”。至少这下验证了，没有交错朋友，张仕杰有时候还是很不错的。"
    print(f"Generated response: {response}")
    
    # AI回复-语音朗读形式
    response_file_name = f"response_{timestamp}.wav"
    response_file_path = os.path.join(responses_dir, response_file_name)  # 将文件保存到 responses 文件夹
    text_to_speech(response, response_file_path)

if __name__ == "__main__":
    main()
