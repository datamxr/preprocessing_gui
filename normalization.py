import librosa
import numpy as np


def normalize_audio(audio_path, target_db):
    audio, sr = librosa.load(audio_path)

    # Calculate the current RMS level
    rms = np.sqrt(np.mean(np.square(audio)))

    # Calculate the gain needed to reach the target level (-8 dB)
    target_gain = 10 ** ((target_db - 20 * np.log10(rms)) / 20)

    # Apply the gain to normalize the audio
    normalized_audio = audio * target_gain

    # Overwrite file
    librosa.output.write_wav(audio_path, normalized_audio, sr)