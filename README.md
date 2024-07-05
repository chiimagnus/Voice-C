# VoiceAI-C 语音助手

这是一个python项目，目前仅可以实现和大模型的单次对话。

语音识别来自[whisper](https://github.com/openai/whisper),
LLM大模型可以任选，可在[huggingface](https://huggingface.co)上下载相应模型，
文本转语音可使用gTTS，或者[coquiTTS](https://github.com/coqui-ai/TTS)

## 1、文件结构

```bash
├───main_g.py
├───main_coqui.py
├───models
├───responses
├───inputs
```

主要程序逻辑全部在 `main.py` 中，`models/` 文件夹存放模型文件。

PS: 你需要单独建立一个`models/`文件夹，而`responses/`、`inputs/`文件夹你单独不需要建立。
`inputs/`存放输入语音
`responses/`存放回复语音

## 2、运行指南

本项目基于 Python 编程语言，建议使用 [Anaconda](https://www.anaconda.com) 配置 Python 环境，当然也可以使用下面的conda命令创建环境～

### 2.1、环境配置

```
conda create -n VoiceAI python=3.11
conda activate VoiceAI

pip install whisper
pip install llama-cpp-python
pip install TTS
pip install gtts
pip install sounddevice
pip install scipy
pip install pydub
```

此外，你可能还需要安装一些系统依赖项。对于pydub，还需要安装FFmpeg，

对于Ubuntu:
```bash
sudo apt-get install ffmpeg
```

对于MacOS (使用Homebrew):
```bash
brew install ffmpeg
```

对于Windows: 你可以从[FFmpeg的官方网站](https://ffmpeg.org/download.html)下载并安装FFmpeg。

### 2.2、模型文件

LLM模型文件可参考[qwen2大模型的量化版本](https://huggingface.co/MaziyarPanahi/Qwen2-1.5B-Instruct-GGUF)。

## 3、鸣谢

1、语音识别基于[whisper](https://github.com/openai/whisper)。

2、文字回复基于[qwen2大模型的量化版本](https://huggingface.co/MaziyarPanahi/Qwen2-1.5B-Instruct-GGUF)。

3、文字转语音基于gTTS或者使用[coquiTTS](https://github.com/coqui-ai/TTS)。

4、作为开发者小白，在此非常感谢[linyiLYi的项目](https://github.com/linyiLYi/voice-assistant)对我的极大帮助。

感谢各位程序工作者对开源社区的贡献！