from faster_whisper import WhisperModel, BatchedInferencePipeline

# Not supported (compute capability > 6.1)
# model = WhisperModel("turbo", device="cuda", compute_type="float16")
# OOM 
# model = WhisperModel("turbo", device="cuda", compute_type="float32")
model = WhisperModel("turbo", device="cuda", compute_type="int8")

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

# locate -i model.bin
# /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/snapshots/edaa852ec7e145841d8ffdb056a99866b5f0a478/model.bin
# /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny.en/snapshots/0d3d19a32d3338f10357c0889762bd8d64bbdeba/model.bin
# /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny/snapshots/d90ca5fe260221311c53c58e660288d3deb8d356/model.bin
# /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/0c94664816ec82be77b20e824c8e8675995b0029/model.bin

# ls -lh /home/hmf/.cache/huggingface/hub/*/snapshots/*
# ls -lh /home/hmf/.cache/huggingface/hub/*/blobs/*
# -rw-rw-r-- 1 hmf hmf 2,3K nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/0351d1d6870005e865747b781b5d7c23ea0459cd
# -rw-rw-r-- 1 hmf hmf 1,1M nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/0adcd01e7c237205d593b707e66dd5d7bc785d2d
# -rw-rw-r-- 1 hmf hmf 2,6M nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/17456db595adc78a973f97d69d8cb50bc87c0b1c
# -rw-rw-r-- 1 hmf hmf  340 nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/931c77a740890c46365c7ae0c9d350ba3cca908f
# -rw-rw-r-- 1 hmf hmf 1,6G nov 27 16:52 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/e76620f83d5f5b69efd3d87e3dc180c1bd21df9fbebacfd4335e5e1efcc018da
# -rw-rw-r-- 1 hmf hmf 1,1M nov 24 11:50 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/blobs/0adcd01e7c237205d593b707e66dd5d7bc785d2d
# -rw-rw-r-- 1 hmf hmf 2,4M nov 24 11:50 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/blobs/3a5e2ba63acdcac9a19ba56cf9bd27f185bfff61
# -rw-rw-r-- 1 hmf hmf 2,9G nov 24 11:55 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/blobs/69f74147e3334731bc3a76048724833325d2ec74642fb52620eda87352e3d4f1
# -rw-rw-r-- 1 hmf hmf 2,4K nov 24 11:50 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/blobs/75336feae814999bae6ccccdecf177639ffc6f9d
# -rw-rw-r-- 1 hmf hmf  340 nov 24 11:50 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3/blobs/931c77a740890c46365c7ae0c9d350ba3cca908f
# -rw-rw-r-- 1 hmf hmf 2,2K nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny/blobs/3baa18e2b321a2f489614607852a729fcd516480
# -rw-rw-r-- 1 hmf hmf 2,2M nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny/blobs/7818adb6de9fa3064d3ff81226fdd675be1f6344
# -rw-rw-r-- 1 hmf hmf 450K nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny/blobs/c9074644d9d1205686f16d411564729461324b75
# -rw-rw-r-- 1 hmf hmf  73M nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny/blobs/dcb76c6586fc06cbdac6dd21f14cfd129cc4cdd9dce19bf4ffa62e59cbe6e6d1
# -rw-rw-r-- 1 hmf hmf 2,1M nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny.en/blobs/15d7bdf9ba25718ca2504eec6a8f02bc55af0a6a
# -rw-rw-r-- 1 hmf hmf  73M nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny.en/blobs/1a5afae06a4db91c975c9a9d78be5cc110ee4ea022ad57d55492e4550e936b2a
# -rw-rw-r-- 1 hmf hmf 2,3K nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny.en/blobs/4065bb3bed375b176d5465be117d2d202e210434
# -rw-rw-r-- 1 hmf hmf 413K nov 24 11:33 /home/hmf/.cache/huggingface/hub/models--Systran--faster-whisper-tiny.en/blobs/ee695b8d3e3c10d488304e04468efec4ca27554a

# ls -lh /home/hmf/.cache/huggingface/hub/*/blobs/* | grep -i turbo
# -rw-rw-r-- 1 hmf hmf 2,3K nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/0351d1d6870005e865747b781b5d7c23ea0459cd
# -rw-rw-r-- 1 hmf hmf 1,1M nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/0adcd01e7c237205d593b707e66dd5d7bc785d2d
# -rw-rw-r-- 1 hmf hmf 2,6M nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/17456db595adc78a973f97d69d8cb50bc87c0b1c
# -rw-rw-r-- 1 hmf hmf  340 nov 27 16:50 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/931c77a740890c46365c7ae0c9d350ba3cca908f
# -rw-rw-r-- 1 hmf hmf 1,6G nov 27 16:52 /home/hmf/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/blobs/e76620f83d5f5b69efd3d87e3dc180c1bd21df9fbebacfd4335e5e1efcc018da
# hmf@gandalf:~/Desktop/notepad/vpn$ 
