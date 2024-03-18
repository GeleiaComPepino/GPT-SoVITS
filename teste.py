import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
AUDIO_FILE = 'teste.wav'
processor = Wav2Vec2Processor.from_pretrained("lgris/wav2vec2-large-xlsr-open-brazilian-portuguese")
model = Wav2Vec2ForCTC.from_pretrained("lgris/wav2vec2-large-xlsr-open-brazilian-portuguese")
speech, rate = librosa.load(AUDIO_FILE, sr=16000)
 
# Tokenizing the input
inputs = processor(speech, return_tensors="pt", sampling_rate=rate).input_values
 
# Model logits
with torch.no_grad():
    logits = model(inputs).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
print(transcription)