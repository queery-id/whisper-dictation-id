# Whisper Dictation - Indonesian 🇮🇩

> **Voice typing for Windows 11 with Indonesian language support**  
> Uses OpenAI Whisper (via Groq API) for accurate speech-to-text

Windows built-in voice typing (`Win + H`) doesn't support Indonesian. This tool solves that!

## ✨ Features

- 🎤 **Indonesian speech recognition** with high accuracy
- ⚡ **Fast transcription** via Groq API (free!)
- ⌨️ **Global hotkey** - works in any application
- 📋 **Auto-paste** transcribed text at cursor position
- 💻 **CPU-friendly** - no GPU required

## 🚀 Quick Start

### 1. Clone & Install

```powershell
git clone https://github.com/queery-id/whisper-dictation-id.git
cd whisper-dictation-id
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

### 2. Get FREE Groq API Key

1. Go to https://console.groq.com/keys
2. Sign up with Google/GitHub
3. Create new API key

### 3. Configure

```powershell
copy src\config.example.py src\config.py
```

Edit `src/config.py` and paste your API key:
```python
GROQ_API_KEY = 'your_api_key_here'
```

### 4. Run

```powershell
# Run normally
.\run.bat

# Or with admin (if hotkey doesn't work)
# Right-click run_admin.bat → Run as Administrator
```

## 📖 Usage

1. Press **`Ctrl + Win + H`** to start recording
2. Speak in Indonesian (or any language)
3. Press **`Ctrl + Win + H`** again to stop
4. Text appears at your cursor position!

## ⚙️ Configuration

Edit `src/config.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `HOTKEY` | `ctrl+win+h` | Toggle recording key |
| `LANGUAGE` | `id` | Language code (`id`, `en`, `auto`) |
| `USE_CLOUD` | `True` | Use Groq API (recommended) |
| `MODEL_SIZE` | `small` | Local model if USE_CLOUD=False |

## 🔧 Troubleshooting

**Hotkey not working?**
- Run as Administrator (`run_admin.bat`)

**Poor accuracy?**
- Make sure `USE_CLOUD = True` in config
- Check your Groq API key is valid

## 📄 License

MIT License - feel free to use and modify!

## 🙏 Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [Groq](https://groq.com) for free API access
