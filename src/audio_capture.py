"""
Audio capture module using sounddevice
"""
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write as write_wav
import tempfile
import os
from config import SAMPLE_RATE


class AudioRecorder:
    """Records audio from microphone"""
    
    def __init__(self, sample_rate: int = SAMPLE_RATE):
        self.sample_rate = sample_rate
        self.recording = False
        self.audio_data = []
        self.stream = None
    
    def _callback(self, indata, frames, time, status):
        """Callback for audio stream"""
        if status:
            print(f"Audio status: {status}")
        if self.recording:
            self.audio_data.append(indata.copy())
    
    def start(self):
        """Start recording"""
        self.audio_data = []
        self.recording = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.float32,
            callback=self._callback
        )
        self.stream.start()
        print("Recording started...")
    
    def stop(self) -> str:
        """Stop recording and save to temp file, returns file path"""
        self.recording = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None
        
        if not self.audio_data:
            print("No audio recorded")
            return None
        
        audio = np.concatenate(self.audio_data, axis=0)
        audio_int16 = (audio * 32767).astype(np.int16)
        
        temp_file = os.path.join(tempfile.gettempdir(), "whisper_dictation_temp.wav")
        write_wav(temp_file, self.sample_rate, audio_int16)
        
        duration = len(audio) / self.sample_rate
        print(f"Recording stopped. Duration: {duration:.1f}s")
        
        return temp_file
    
    def is_recording(self) -> bool:
        return self.recording
