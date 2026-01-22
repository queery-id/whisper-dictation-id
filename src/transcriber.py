"""
Whisper transcription module using faster-whisper
"""
from faster_whisper import WhisperModel
from config import MODEL_SIZE, DEVICE, COMPUTE_TYPE, LANGUAGE, USE_CLOUD, GROQ_API_KEY

_model = None


def get_model() -> WhisperModel:
    """Get or initialize the Whisper model"""
    global _model
    if _model is None:
        print(f"Loading Whisper model '{MODEL_SIZE}'...")
        _model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
        print("Model loaded successfully!")
    return _model


def transcribe_local(audio_path: str) -> str:
    """Transcribe audio using local faster-whisper model"""
    model = get_model()
    language = None if LANGUAGE == 'auto' else LANGUAGE
    segments, info = model.transcribe(
        audio_path, language=language, beam_size=5,
        vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500)
    )
    text = " ".join([segment.text.strip() for segment in segments])
    if LANGUAGE == 'auto':
        print(f"Detected language: {info.language}")
    return text


def transcribe_cloud(audio_path: str) -> str:
    """Transcribe audio using Groq API"""
    try:
        from groq import Groq
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not set in config.py")
        client = Groq(api_key=GROQ_API_KEY)
        with open(audio_path, "rb") as f:
            transcription = client.audio.transcriptions.create(
                file=(audio_path, f.read()),
                model="whisper-large-v3",
                language=LANGUAGE if LANGUAGE != 'auto' else None,
                response_format="text"
            )
        return transcription.strip()
    except Exception as e:
        print(f"Cloud transcription error: {e}")
        return ""


def transcribe(audio_path: str) -> str:
    """Main transcription function"""
    if USE_CLOUD:
        print("Using cloud transcription (Groq)...")
        return transcribe_cloud(audio_path)
    else:
        print("Using local transcription...")
        return transcribe_local(audio_path)
