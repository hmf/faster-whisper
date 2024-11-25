```shell
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ pip install -e .[dev]
Obtaining file:///mnt/ssd2/hmf/VSCodeProjects/faster-whisper
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: ctranslate2<5,>=4.0 in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (4.5.0)
Requirement already satisfied: huggingface_hub>=0.13 in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (0.26.2)
Requirement already satisfied: tokenizers<1,>=0.13 in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (0.20.3)
Requirement already satisfied: onnxruntime<2,>=1.14 in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (1.20.1)
Requirement already satisfied: av>=11 in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (13.1.0)
Requirement already satisfied: tqdm in ./.venv/lib/python3.12/site-packages (from faster-whisper==1.1.0) (4.67.0)
Collecting black==23.* (from faster-whisper==1.1.0)
  Downloading black-23.12.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (68 kB)
Collecting flake8==6.* (from faster-whisper==1.1.0)
  Downloading flake8-6.1.0-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting isort==5.* (from faster-whisper==1.1.0)
  Downloading isort-5.13.2-py3-none-any.whl.metadata (12 kB)
Collecting pytest==7.* (from faster-whisper==1.1.0)
  Downloading pytest-7.4.4-py3-none-any.whl.metadata (7.9 kB)
Requirement already satisfied: click>=8.0.0 in ./.venv/lib/python3.12/site-packages (from black==23.*->faster-whisper==1.1.0) (8.1.7)
Collecting mypy-extensions>=0.4.3 (from black==23.*->faster-whisper==1.1.0)
  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Requirement already satisfied: packaging>=22.0 in ./.venv/lib/python3.12/site-packages (from black==23.*->faster-whisper==1.1.0) (24.2)
Collecting pathspec>=0.9.0 (from black==23.*->faster-whisper==1.1.0)
  Downloading pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
Collecting platformdirs>=2 (from black==23.*->faster-whisper==1.1.0)
  Downloading platformdirs-4.3.6-py3-none-any.whl.metadata (11 kB)
Collecting mccabe<0.8.0,>=0.7.0 (from flake8==6.*->faster-whisper==1.1.0)
  Downloading mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
Collecting pycodestyle<2.12.0,>=2.11.0 (from flake8==6.*->faster-whisper==1.1.0)
  Downloading pycodestyle-2.11.1-py2.py3-none-any.whl.metadata (4.5 kB)
Collecting pyflakes<3.2.0,>=3.1.0 (from flake8==6.*->faster-whisper==1.1.0)
  Downloading pyflakes-3.1.0-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting iniconfig (from pytest==7.*->faster-whisper==1.1.0)
  Downloading iniconfig-2.0.0-py3-none-any.whl.metadata (2.6 kB)
Collecting pluggy<2.0,>=0.12 (from pytest==7.*->faster-whisper==1.1.0)
  Downloading pluggy-1.5.0-py3-none-any.whl.metadata (4.8 kB)
Requirement already satisfied: setuptools in ./.venv/lib/python3.12/site-packages (from ctranslate2<5,>=4.0->faster-whisper==1.1.0) (75.6.0)
Requirement already satisfied: numpy in ./.venv/lib/python3.12/site-packages (from ctranslate2<5,>=4.0->faster-whisper==1.1.0) (2.1.3)
Requirement already satisfied: pyyaml<7,>=5.3 in ./.venv/lib/python3.12/site-packages (from ctranslate2<5,>=4.0->faster-whisper==1.1.0) (6.0.2)
Requirement already satisfied: filelock in ./.venv/lib/python3.12/site-packages (from huggingface_hub>=0.13->faster-whisper==1.1.0) (3.16.1)
Requirement already satisfied: fsspec>=2023.5.0 in ./.venv/lib/python3.12/site-packages (from huggingface_hub>=0.13->faster-whisper==1.1.0) (2024.9.0)
Requirement already satisfied: requests in ./.venv/lib/python3.12/site-packages (from huggingface_hub>=0.13->faster-whisper==1.1.0) (2.32.3)
Requirement already satisfied: typing-extensions>=3.7.4.3 in ./.venv/lib/python3.12/site-packages (from huggingface_hub>=0.13->faster-whisper==1.1.0) (4.12.2)
Requirement already satisfied: coloredlogs in ./.venv/lib/python3.12/site-packages (from onnxruntime<2,>=1.14->faster-whisper==1.1.0) (15.0.1)
Requirement already satisfied: flatbuffers in ./.venv/lib/python3.12/site-packages (from onnxruntime<2,>=1.14->faster-whisper==1.1.0) (24.3.25)
Requirement already satisfied: protobuf in ./.venv/lib/python3.12/site-packages (from onnxruntime<2,>=1.14->faster-whisper==1.1.0) (5.28.3)
Requirement already satisfied: sympy in ./.venv/lib/python3.12/site-packages (from onnxruntime<2,>=1.14->faster-whisper==1.1.0) (1.13.1)
Requirement already satisfied: humanfriendly>=9.1 in ./.venv/lib/python3.12/site-packages (from coloredlogs->onnxruntime<2,>=1.14->faster-whisper==1.1.0) (10.0)
Requirement already satisfied: charset-normalizer<4,>=2 in ./.venv/lib/python3.12/site-packages (from requests->huggingface_hub>=0.13->faster-whisper==1.1.0) (3.4.0)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests->huggingface_hub>=0.13->faster-whisper==1.1.0) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.12/site-packages (from requests->huggingface_hub>=0.13->faster-whisper==1.1.0) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests->huggingface_hub>=0.13->faster-whisper==1.1.0) (2024.8.30)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./.venv/lib/python3.12/site-packages (from sympy->onnxruntime<2,>=1.14->faster-whisper==1.1.0) (1.3.0)
Downloading black-23.12.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 9.9 MB/s eta 0:00:00
Downloading flake8-6.1.0-py2.py3-none-any.whl (58 kB)
Downloading isort-5.13.2-py3-none-any.whl (92 kB)
Downloading pytest-7.4.4-py3-none-any.whl (325 kB)
Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Downloading pathspec-0.12.1-py3-none-any.whl (31 kB)
Downloading platformdirs-4.3.6-py3-none-any.whl (18 kB)
Downloading pluggy-1.5.0-py3-none-any.whl (20 kB)
Downloading pycodestyle-2.11.1-py2.py3-none-any.whl (31 kB)
Downloading pyflakes-3.1.0-py2.py3-none-any.whl (62 kB)
Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Building wheels for collected packages: faster-whisper
  Building editable for faster-whisper (pyproject.toml) ... done
  Created wheel for faster-whisper: filename=faster_whisper-1.1.0-0.editable-py3-none-any.whl size=9209 sha256=a2e71444f821f33d7b67978c22b411330803a4c3ebf2fdba29f8edcf6c89924f
  Stored in directory: /tmp/pip-ephem-wheel-cache-c4oqecod/wheels/1a/f2/ec/cf70be1263b8658eb60bd50c039679c9b2e1b7e64e1622e1b8
Successfully built faster-whisper
Installing collected packages: pyflakes, pycodestyle, pluggy, platformdirs, pathspec, mypy-extensions, mccabe, isort, iniconfig, pytest, flake8, black, faster-whisper
Successfully installed black-23.12.1 faster-whisper-1.1.0 flake8-6.1.0 iniconfig-2.0.0 isort-5.13.2 mccabe-0.7.0 mypy-extensions-1.0.0 pathspec-0.12.1 platformdirs-4.3.6 pluggy-1.5.0 pycodestyle-2.11.1 pyflakes-3.1.0 pytest-7.4.4
```

```shell
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ pytest -v tests/
=============================================================== test session starts ===============================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.5.0 -- /mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/python
cachedir: .pytest_cache
rootdir: /mnt/ssd2/hmf/VSCodeProjects/faster-whisper
collected 17 items                                                                                                                                

tests/test_tokenizer.py::test_suppressed_tokens_minus_1 PASSED                                                                              [  5%]
tests/test_tokenizer.py::test_suppressed_tokens_minus_value PASSED                                                                          [ 11%]
tests/test_tokenizer.py::test_split_on_unicode PASSED                                                                                       [ 17%]
tests/test_transcribe.py::test_supported_languages PASSED                                                                                   [ 23%]
tests/test_transcribe.py::test_transcribe Fatal Python error: Aborted

Thread 0x00007dd582a006c0 (most recent call first):
  File "/usr/lib/python3.12/threading.py", line 359 in wait
  File "/usr/lib/python3.12/threading.py", line 655 in wait
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/tqdm/_monitor.py", line 60 in run
  File "/usr/lib/python3.12/threading.py", line 1073 in _bootstrap_inner
  File "/usr/lib/python3.12/threading.py", line 1030 in _bootstrap

Thread 0x00007dd5834006c0 (most recent call first):
  File "/usr/lib/python3.12/threading.py", line 359 in wait
  File "/usr/lib/python3.12/threading.py", line 655 in wait
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/tqdm/_monitor.py", line 60 in run
  File "/usr/lib/python3.12/threading.py", line 1073 in _bootstrap_inner
  File "/usr/lib/python3.12/threading.py", line 1030 in _bootstrap

Thread 0x00007dd6759ed080 (most recent call first):
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 1345 in encode
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 1764 in detect_language
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 887 in transcribe
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/tests/test_transcribe.py", line 16 in test_transcribe
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/python.py", line 194 in pytest_pyfunc_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/python.py", line 1792 in runtest
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 169 in pytest_runtest_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 262 in <lambda>
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 341 in from_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 261 in call_runtest_hook
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 222 in call_and_report
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 133 in runtestprotocol
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 114 in pytest_runtest_protocol
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 350 in pytest_runtestloop
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 325 in _main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 271 in wrap_session
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 318 in pytest_cmdline_main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 169 in main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 192 in console_main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/pytest", line 8 in <module>

Extension modules: av._core, av.logging, av.bytesource, av.buffer, av.audio.format, av.enum, av.error, av.utils, av.option, av.descriptor, av.container.pyio, av.dictionary, av.format, av.stream, av.container.streams, av.sidedata.motionvectors, av.sidedata.sidedata, av.opaque, av.packet, av.container.input, av.container.output, av.container.core, av.codec.context, av.video.format, av.video.reformatter, av.plane, av.video.plane, av.video.frame, av.video.stream, av.codec.codec, av.frame, av.audio.layout, av.audio.plane, av.audio.frame, av.audio.stream, av.filter.pad, av.filter.link, av.filter.context, av.filter.graph, av.filter.filter, av.audio.resampler, av.audio.codeccontext, av.audio.fifo, av.bitstream, av.video.codeccontext, numpy._core._multiarray_umath, numpy.linalg._umath_linalg, torch._C, torch._C._dynamo.autograd_compiler, torch._C._dynamo.eval_frame, torch._C._dynamo.guards, torch._C._dynamo.utils, torch._C._fft, torch._C._linalg, torch._C._nested, torch._C._nn, torch._C._sparse, torch._C._special, yaml._yaml, charset_normalizer.md, requests.packages.charset_normalizer.md, requests.packages.chardet.md, markupsafe._speedups (total: 63)
Aborted (core dumped)
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ 
```

```shell
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ pytest -v tests/test_utils.py 
=============================================================== test session starts ===============================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.5.0 -- /mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/python
cachedir: .pytest_cache
rootdir: /mnt/ssd2/hmf/VSCodeProjects/faster-whisper
collected 3 items                                                                                                                                 

tests/test_utils.py::test_available_models PASSED                                                                                           [ 33%]
tests/test_utils.py::test_download_model PASSED                                                                                             [ 66%]
tests/test_utils.py::test_download_model_in_cache PASSED                                                                                    [100%]

================================================================ warnings summary =================================================================
tests/test_utils.py::test_download_model
  /mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py:834: UserWarning: `local_dir_use_symlinks` parameter is deprecated and will be ignored. The process to download files to a local folder has been updated and do not rely on symlinks anymore. You only need to pass a destination folder as`local_dir`.
  For more details, check out https://huggingface.co/docs/huggingface_hub/main/en/guides/download#download-files-to-local-folder.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================== 3 passed, 1 warning in 9.59s ===========================================================
```

```shell
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ pytest -v tests/test_tokenizer.py 
=============================================================== test session starts ===============================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.5.0 -- /mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/python
cachedir: .pytest_cache
rootdir: /mnt/ssd2/hmf/VSCodeProjects/faster-whisper
collected 3 items                                                                                                                                 

tests/test_tokenizer.py::test_suppressed_tokens_minus_1 PASSED                                                                              [ 33%]
tests/test_tokenizer.py::test_suppressed_tokens_minus_value PASSED                                                                          [ 66%]
tests/test_tokenizer.py::test_split_on_unicode PASSED                                                                                       [100%]

================================================================ 3 passed in 3.51s ================================================================
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ 
```

```shell
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ pytest -v tests/test_transcribe.py 
=============================================================== test session starts ===============================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.5.0 -- /mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/python
cachedir: .pytest_cache
rootdir: /mnt/ssd2/hmf/VSCodeProjects/faster-whisper
collected 11 items                                                                                                                                

tests/test_transcribe.py::test_supported_languages PASSED                                                                                   [  9%]
tests/test_transcribe.py::test_transcribe Fatal Python error: Aborted

Thread 0x00007e94ed2006c0 (most recent call first):
  File "/usr/lib/python3.12/threading.py", line 359 in wait
  File "/usr/lib/python3.12/threading.py", line 655 in wait
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/tqdm/_monitor.py", line 60 in run
  File "/usr/lib/python3.12/threading.py", line 1073 in _bootstrap_inner
  File "/usr/lib/python3.12/threading.py", line 1030 in _bootstrap

Thread 0x00007e95da394080 (most recent call first):
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 1345 in encode
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 1764 in detect_language
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/faster_whisper/transcribe.py", line 887 in transcribe
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/tests/test_transcribe.py", line 16 in test_transcribe
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/python.py", line 194 in pytest_pyfunc_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/python.py", line 1792 in runtest
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 169 in pytest_runtest_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 262 in <lambda>
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 341 in from_call
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 261 in call_runtest_hook
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 222 in call_and_report
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 133 in runtestprotocol
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/runner.py", line 114 in pytest_runtest_protocol
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 350 in pytest_runtestloop
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 325 in _main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 271 in wrap_session
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/main.py", line 318 in pytest_cmdline_main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 169 in main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 192 in console_main
  File "/mnt/ssd2/hmf/VSCodeProjects/faster-whisper/.venv/bin/pytest", line 8 in <module>

Extension modules: numpy._core._multiarray_umath, numpy.linalg._umath_linalg, av._core, av.logging, av.bytesource, av.buffer, av.audio.format, av.enum, av.error, av.utils, av.option, av.descriptor, av.container.pyio, av.dictionary, av.format, av.stream, av.container.streams, av.sidedata.motionvectors, av.sidedata.sidedata, av.opaque, av.packet, av.container.input, av.container.output, av.container.core, av.codec.context, av.video.format, av.video.reformatter, av.plane, av.video.plane, av.video.frame, av.video.stream, av.codec.codec, av.frame, av.audio.layout, av.audio.plane, av.audio.frame, av.audio.stream, av.filter.pad, av.filter.link, av.filter.context, av.filter.graph, av.filter.filter, av.audio.resampler, av.audio.codeccontext, av.audio.fifo, av.bitstream, av.video.codeccontext, torch._C, torch._C._dynamo.autograd_compiler, torch._C._dynamo.eval_frame, torch._C._dynamo.guards, torch._C._dynamo.utils, torch._C._fft, torch._C._linalg, torch._C._nested, torch._C._nn, torch._C._sparse, torch._C._special, yaml._yaml, charset_normalizer.md, requests.packages.charset_normalizer.md, requests.packages.chardet.md, markupsafe._speedups (total: 63)
Aborted (core dumped)
(.venv) hmf@gandalf:/mnt/ssd2/hmf/VSCodeProjects/faster-whisper$ 
```

https://www.geeksforgeeks.org/how-to-verify-cudnn-installation/

hmf@gandalf:~$ cat /usr/include/x86_64-linux-gnu/cudnn_v*.h | grep CUDNN_MAJOR -A 2
#define CUDNN_MAJOR 8
#define CUDNN_MINOR 9
#define CUDNN_PATCHLEVEL 7
--
#define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)

/* cannot use constexpr here since this is a C-only file */


hmf@gandalf:~$ cat /usr/local/cuda/include/cublas_api.h | grep CUBLAS_VER
#define CUBLAS_VER_MAJOR 12
#define CUBLAS_VER_MINOR 6
#define CUBLAS_VER_PATCH 3
#define CUBLAS_VER_BUILD 3
#define CUBLAS_VERSION (CUBLAS_VER_MAJOR * 10000 + CUBLAS_VER_MINOR * 100 + CUBLAS_VER_PATCH)

https://forums.developer.nvidia.com/t/unable-to-verify-cudnn-installation-on-linux-ubuntu-20-04/203155/11
https://askubuntu.com/questions/1520509/issues-installing-cuda-and-cudnn-on-ubuntu-24-04
https://gist.github.com/denguir/b21aa66ae7fb1089655dd9de8351a202


https://serverspace.io/support/help/configure-repositories-on-ubuntu-20-04/
 ls /etc/apt/
apt.conf.d   keyrings       sources.list    sources.list.2  sources.list.distUpgrade  trusted.gpg   trusted.gpg.d
auth.conf.d  preferences.d  sources.list.1  sources.list.d  sources.list.save         trusted.gpg~

hmf@gandalf:~$ cat /etc/apt/sources.list
# Ubuntu sources have moved to /etc/apt/sources.list.d/ubuntu.sources


sudo apt install nvidia-cuda-toolkit
sudo apt install nvidia-cudnn

hmf@gandalf:~$ sudo apt install nvidia-cudnn
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libatomic1:i386 libdrm-amdgpu1:i386 libdrm-intel1:i386 libdrm-nouveau2:i386 libdrm-radeon1:i386 libedit2:i386 libegl-mesa0:i386 libegl1:i386 libelf1t64:i386
  libexpat1:i386 libgbm1:i386 libgl1:i386 libgl1-mesa-dri:i386 libglapi-mesa:i386 libgles2:i386 libglvnd0:i386 libglx-mesa0:i386 libglx0:i386 libicu74:i386
  libllvm17t64:i386 libopengl0:i386 libpciaccess0:i386 libsensors5:i386 libstdc++6:i386 libvulkan1:i386 libx11-xcb1:i386 libxcb-dri2-0:i386 libxcb-dri3-0:i386
  libxcb-glx0:i386 libxcb-present0:i386 libxcb-randr0:i386 libxcb-shm0:i386 libxcb-sync1:i386 libxcb-xfixes0:i386 libxfixes3:i386 libxml2:i386 libxshmfence1:i386
  libxxf86vm1:i386 mesa-vulkan-drivers:i386
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  nvidia-cuda-toolkit-gcc
The following NEW packages will be installed:
  nvidia-cuda-toolkit-gcc nvidia-cudnn
0 upgraded, 2 newly installed, 0 to remove and 6 not upgraded.
Need to get 33,9 kB of archives.
After this operation, 152 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://pt.archive.ubuntu.com/ubuntu noble/multiverse amd64 nvidia-cuda-toolkit-gcc amd64 12.0.1-4build4 [16,5 kB]
Get:2 http://pt.archive.ubuntu.com/ubuntu noble/multiverse amd64 nvidia-cudnn amd64 8.9.2.26~cuda12+3 [17,4 kB]
Fetched 33,9 kB in 0s (173 kB/s)       
Preconfiguring packages ...
Selecting previously unselected package nvidia-cuda-toolkit-gcc.
(Reading database ... 325493 files and directories currently installed.)
Preparing to unpack .../nvidia-cuda-toolkit-gcc_12.0.1-4build4_amd64.deb ...
Unpacking nvidia-cuda-toolkit-gcc (12.0.1-4build4) ...
Selecting previously unselected package nvidia-cudnn.
Preparing to unpack .../nvidia-cudnn_8.9.2.26~cuda12+3_amd64.deb ...
Unpacking nvidia-cudnn (8.9.2.26~cuda12+3) ...
dpkg: error processing archive /var/cache/apt/archives/nvidia-cudnn_8.9.2.26~cuda12+3_amd64.deb (--unpack):
 trying to overwrite '/usr/lib/x86_64-linux-gnu/libcudnn.so', which is also in package libcudnn8-dev 8.9.7.29-1+cuda12.2
Errors were encountered while processing:
 /var/cache/apt/archives/nvidia-cudnn_8.9.2.26~cuda12+3_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

------------------------------------

https://github.com/SYSTRAN/faster-whisper
cuBLAS for CUDA 12
cuDNN 9 for CUDA 12


dpkg -l | grep nvidia

sudo apt-get --purge remove "*cublas*" "cuda*"
sudo apt-get --purge remove "*cublas*" "*cufft*" "*curand*" \
 "*cusolver*" "*cusparse*" "*npp*" "*nvjpeg*" "cuda*" "nsight*" 
sudo apt-get --purge remove "*nvidia*" "libxnvctrl*"

sudo apt-get install ubuntu-desktop


X sudo apt-get remove --purge '^nvidia-.*'
the .* in the end means (Purge everything that begins (^) with the name nvidia-)

BUT

above command will also remove the nvidia-common package and the nvidia-common package has as a dependency the ubuntu-desktop package.

So after above command you should also give the installation command for ubuntu-desktop package

sudo apt-get install ubuntu-desktop


https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#meta-packages


sudo apt-get install cuda-toolkit
sudo dpkg -i cuda-repo-cross-<arch>-<distro>-X-Y-local-<version>*_all.deb
<arch>-<distro> = sbsa-ubuntu2404
sudo apt-get update


---------------------------

sudo apt-get --purge remove "*cublas*" "*cufft*" "*curand*" \
 "*cusolver*" "*cusparse*" "*npp*" "*nvjpeg*" "cuda*" "nsight*" 

reboot

sudo apt autoremove

reboot

sudo apt-key del 7fa2af80


https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04

Remote 

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6

sudo apt-get install cuda-toolkit
sudo apt-get install nvidia-gds

Building module:
Cleaning build area...
'make' -j32 KVER=6.8.0-49-generic IGNORE_CC_MISMATCH='1'........................
Signing module /var/lib/dkms/nvidia-fs/2.22.3/build/nvidia-fs.ko
Cleaning build area...
Deprecated feature: REMAKE_INITRD (/var/lib/dkms/nvidia-fs/2.22.3/source/dkms.conf)

nvidia-fs.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.8.0-49-generic/updates/dkms/
depmod.....
modprobe: ERROR: could not insert 'nvidia_fs': Unknown symbol in module, or unknown parameter (see dmesg)

*************************************************************************
*** Reboot your computer and verify that the NVIDIA filesystem driver ***
*** can be loaded.                                                    ***
*************************************************************************

sudo reboot

sudo apt-get update
sudo apt-get install cudnn9-cuda-12

https://developer.nvidia.com/hpc-sdk-downloads
Bundled with the newest CUDA version (12.6)




Local X

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin
sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda-repo-ubuntu2404-12-6-local_12.6.3-560.35.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2404-12-6-local_12.6.3-560.35.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2404-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6

https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html


---------------------

from sudo dmesg
drm:nv_drm_master_set [nvidia_drm]] *ERROR* [nvidia-drm] [GPU ID 0x00000100] Failed to grab modeset ownership

https://askubuntu.com/questions/1506606/options-nvidia-drm-modeset-1-in-place-but-still-have-the-modeset-error

from sudo dmesg
nvidia_fs: module using GPL-only symbols uses symbols nvidia_p2p_dma_unmap_pages from proprietary module nvidia.



pytest -v tests/test_utils.py
pytest -v tests/test_tokenizer.py 
pytest -v tests/test_transcribe.py 
pytest tests/


https://www.leadtek.com/eng/products/workstation_graphics(2)/nvidia_quadro_p1000(10773)/detail


https://developer.nvidia.com/cuda-gpus
https://developer.nvidia.com/cuda-gpus#compute
Quadro P1000 	6.1
https://github.com/SYSTRAN/faster-whisper/issues/42
https://github.com/SYSTRAN/faster-whisper/issues/42#issuecomment-1681736015
"As explained above, FP16 is only enabled for GPUs with Tensor Cores (Compute Capability 7.0 and above). You can set the environment variable to bypass this check.

int8 should work on the P40 which has Compute Capability 6.1."

----------------------

ssh ubuntu@10.61.14.231

