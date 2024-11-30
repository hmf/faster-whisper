from faster_whisper import WhisperModel, BatchedInferencePipeline

# Batched mode

# Models are large and downloaded to the following cache folder
# ls -lh /home/hmf/.cache/huggingface/hub/*/snapshots/*
# ls -lh /home/hmf/.cache/huggingface/hub/*/blobs/*

# Available models
# https://github.com/SYSTRAN/faster-whisper/blob/97a4785fa13d067c300f8b6e40c4381ad0381c02/faster_whisper/utils.py#L12

# Not supported (compute capability > 6.1)
# model = WhisperModel("turbo", device="cuda", compute_type="float16")
# OOM 
# model = WhisperModel("turbo", device="cuda", compute_type="float32")
model = WhisperModel("turbo", device="cuda", compute_type="int8", download_root="./models")

batched_model = BatchedInferencePipeline(model=model)
# segments, info = batched_model.transcribe("audio.mp3", batch_size=16)
# sample = "./tests/data/hotwords.mp3"
# sample = "./tests/data/jfk.flac"
# sample = "./tests/data/multilingual.mp3"
sample = "./tests/data/physicsworks.wav" # longest processing
# sample = "./tests/data/stereo_diarization.wav"
segments, info = batched_model.transcribe(sample, batch_size=16)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

