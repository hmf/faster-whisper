from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
# Failed
# model = WhisperModel(model_size, device="cuda", compute_type="float16")
# New
# Failed, RuntimeError: CUDA failed with error out of memory
# model = WhisperModel(model_size, device="cuda", compute_type="float32")
# Same failed
# model = WhisperModel(model_size, device="cuda")
# Ok
# model = WhisperModel(model_size, device="cuda", compute_type="int8")
model = WhisperModel(model_size, device="cuda")

# or run on GPU with INT8
# Failed
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# Ok 
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# original segments, info = model.transcribe("audio.mp3", beam_size=5)
# sample = "./tests/data/hotwords.mp3"
# sample = "./tests/data/jfk.flac"
sample = "./tests/data/multilingual.mp3"
# sample = "./tests/data/physicsworks.wav" # longest processing
# sample = "./tests/data/stereo_diarization.wav"
segments, info = model.transcribe(sample, beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    