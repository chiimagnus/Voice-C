from llama_cpp import Llama
import whisper
from gtts import gTTS
import sounddevice as sd
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
from datetime import datetime
import os

# 创建 responses 文件夹（如果不存在）
responses_dir = "responses"
os.makedirs(responses_dir, exist_ok=True)

# gTTS播放回复文本
def text_to_speech(text,response_path):
    try:
        tts = gTTS(text=text, lang='zh')
        tts.save(response_path)
        
        # 转换MP3为WAV，这是因为gTTS无法保存.wav格式
        audio = AudioSegment.from_mp3(response_path)
        wav_response_path = response_path.replace(".mp3", ".wav")
        audio.export(wav_response_path, format="wav")
        
        # 播放音频
        fs, data = wavfile.read(wav_response_path)
        sd.play(data, fs)
        sd.wait()

        # 删除临时的.mp3文件
        os.remove(response_path)
    except Exception as e:
        print(f"Error in text_to_speech: {e}")


def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 获取当前时间戳并格式化为字符串

    # AI回复-文本形式
    response = "gtts:怎样旅行才能收获比较大呢？"
    print(f"Generated response: {response}")
    
    # AI回复-语音朗读形式
    response_file_name = f"response_{timestamp}.mp3"
    response_file_path = os.path.join(responses_dir, response_file_name)  # 将文件保存到 responses 文件夹
    text_to_speech(response, response_file_path)

if __name__ == "__main__":
    main()