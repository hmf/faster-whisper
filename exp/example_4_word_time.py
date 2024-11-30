from faster_whisper import WhisperModel

# Distilled model

# https://huggingface.co/distil-whisper/distil-large-v3
# " It [is] the knowledge distilled version of OpenAI's Whisper large-v3, the latest and most performant Whisper model to date."
model_size = "distil-large-v3"

# Models are large and downloaded to the following cache folder
# ls -lh /home/hmf/.cache/huggingface/hub/*/snapshots/*
# ls -lh /home/hmf/.cache/huggingface/hub/*/blobs/*

# Not supported, compute capability > 6.1
# model = WhisperModel(model_size, device="cuda", compute_type="float16", download_root="./models")
# OK
# model = WhisperModel(model_size, device="cuda", compute_type="float32", download_root="./models")
# OK
model = WhisperModel(model_size, device="cuda", compute_type="int8", download_root="./models")
# OK, long time
# model = WhisperModel(model_size, device="cpu", compute_type="float32", download_root="./models")
# model = WhisperModel(model_size, device="cpu", compute_type="int16", download_root="./models")
# model = WhisperModel(model_size, device="cpu", compute_type="int8", download_root="./models")

# sample = "./tests/data/hotwords.mp3"
# sample = "./tests/data/jfk.flac"
# sample = "./tests/data/multilingual.mp3"
sample = "./tests/data/physicsworks.wav" # longest processing
# sample = "./tests/data/stereo_diarization.wav"
# original segments, info = model.transcribe("audio.mp3", beam_size=5, language="en", condition_on_previous_text=False)
# Ok
# segments, info = model.transcribe(sample, beam_size=5, language="en", condition_on_previous_text=False)
segments, info = model.transcribe(sample, beam_size=5, condition_on_previous_text=False, word_timestamps=True)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    if segment.words != None:
        for word in segment.words:
            print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

