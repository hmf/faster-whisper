from faster_whisper import WhisperModel

model_size = "large-v3"

# Models are large and downloaded to the following cache folder
# ls -lh /home/hmf/.cache/huggingface/hub/*/snapshots/*
# ls -lh /home/hmf/.cache/huggingface/hub/*/blobs/*

# Available models
# https://github.com/SYSTRAN/faster-whisper/blob/97a4785fa13d067c300f8b6e40c4381ad0381c02/faster_whisper/utils.py#L12

# Run on GPU with FP16
# Failed
# model = WhisperModel(model_size, device="cuda", compute_type="float16")
# New
# Failed, RuntimeError: CUDA failed with error out of memory
# model = WhisperModel(model_size, device="cuda", compute_type="float32")
# Same failed
# model = WhisperModel(model_size, device="cuda")
# Ok
# but: https://github.com/SYSTRAN/faster-whisper/discussions/1178
# model = WhisperModel(model_size, device="cuda", compute_type="int8", download_root="./models")
model = WhisperModel(model_size, device="cuda", compute_type="int8", download_root="./models")

# or run on GPU with INT8
# Failed
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# Ok 
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# original segments, info = model.transcribe("audio.mp3", beam_size=5)
# sample = "./tests/data/hotwords.mp3"
# sample = "./tests/data/jfk.flac"
# sample = "./tests/data/multilingual.mp3"
sample = "./tests/data/physicsworks.wav" # longest processing
# sample = "./tests/data/stereo_diarization.wav"
print("Transcribing....")
# GPU: Translates to NL
segments, info = model.transcribe(sample, beam_size=5)
# GPU: Force EN
# segments, info = model.transcribe(sample, beam_size=5, language= 'en')
# GPU: EN output but fail due to OOM
# segments, info = model.transcribe(sample, beam_size=8)
# GPU: NL output but fail due to OOM
# segments, info = model.transcribe(sample, beam_size=6)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    