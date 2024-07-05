from llama_cpp import Llama
import whisper
from gtts import gTTS
import sounddevice as sd
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
from datetime import datetime
import os

# 创建 inputs、responses 文件夹（如果不存在）
inputs_dir = "inputs"
os.makedirs(inputs_dir, exist_ok=True)
responses_dir = "responses"
os.makedirs(responses_dir, exist_ok=True)

# 加载 Whisper 模型
whisper_model = whisper.load_model("small")

# 加载 Yi-1.5-6B-Chat.GGUF 模型
model_path = "./models/Yi-1.5-6B-Chat.Q2_K.gguf"
llm_model = Llama(model_path)

# 录音
def record_audio(duration=10, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # 等待录音结束
    print("Recording complete.")
    return audio

# 保存录音文件
def save_audio(audio, file_path, fs=44100):
    wavfile.write(file_path, fs, audio)

# 录音的识别
def recognize_speech(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result['text']

# AI生成回复文本
def generate_response(text):
    response = llm_model(text, max_tokens=100, top_p=0.95, top_k=60)
    return response['choices'][0]['text']

# gTTS播放回复文本
def text_to_speech(text,response_path):
    try:
        tts = gTTS(text=text, lang='zh')
        tts.save(response_path)
        
        # 转换MP3为WAV
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


# 主函数
def main():
    # 录音
    audio = record_audio()
    
    # 保存录音文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 获取当前时间戳并格式化为字符串
    input_file_name = f"input_{timestamp}.wav"
    input_file_path = os.path.join(inputs_dir, input_file_name)  # 将文件保存到 inputs 文件夹
    save_audio(audio, input_file_path)

    # 语言识别并且输出文本
    text = recognize_speech(input_file_path)
    print(f"Recognized text: {text}")
    
    # AI回复-文本形式
    response = generate_response(text)
    print(f"Generated response: {response}")
    
    # AI回复-语音朗读形式
    #text_to_speech(response)
    response_file_name = f"response_{timestamp}.mp3"
    response_file_path = os.path.join(responses_dir, response_file_name)  # 将文件保存到 responses 文件夹
    text_to_speech(response, response_file_path)

if __name__ == "__main__":
    main()