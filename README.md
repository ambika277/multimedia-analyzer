# Multimedia Lab 

A versatile Python toolkit combining comprehensive multimedia inspection (images, audio, video) with zero-shot voice cloning and speech generation.

Overview

This repository hosts two integrated multimedia subprojects:

Multimedia Analyzer (multimedia/multimedia_analyzer/): Deep metadata extraction, integrity verification, technical stream inspection, and automated report generation for image, audio, and video assets.

Voice Cloning Studio (voice-cloning/): Instant zero-shot voice synthesis and text-to-speech generation powered by modern deep learning models.

Directory Architecture

multimedia-analyzer/
│
├── multimedia/
│   └── multimedia_analyzer/
│       ├── audio_analyzer.py      # Audio parsing logic and metadata extraction
│       ├── image_analyzer.py      # Image properties and EXIF tag reader
│       ├── video_analyzer.py      # Video stream and container analyzer
│       ├── file_utils.py          # Shared filesystem helpers and validation
│       ├── report_generator.py    # Report compiler and JSON formatter
│       └── main.py                # Analyzer CLI entry point
│
├── voice-cloning/
│   ├── app.py                     # Voice cloning and synthesis execution script
│   ├── samples/                   # Reference audio samples (.wav, .mp3)
│   │   └── sample.wav
│   ├── outputs/                   # Generated speech output files
│   │   └── cloned_speech.wav
│   ├── requirements.txt           # Voice cloning dependencies
│   └── .env.example               # Environment template (optional)
│
├── reports/                       # Generated analysis reports
│   └── report.json
│
├── .gitignore                     # Git tracking exclusions
├── requirements.txt               # Root analyzer package dependencies
└── README.md                      # Project documentation


Key Features

1. Multimedia Analyzer

Image Analysis (image_analyzer.py):

Dimensions, color mode (RGB, RGBA, Grayscale), and container format.

Embedded EXIF metadata inspection (camera make/model, timestamps, orientation, ISO).

Compression efficiency and artifact assessment.

Audio Analysis (audio_analyzer.py):

Sample rate, channel count (mono/stereo/surround), bit depth, and bitrate.

Container and codec detection across MP3, WAV, FLAC, and AAC.

Tag parsing and audio stream header inspection.

Video Analysis (video_analyzer.py):

Container formats, stream counts, video codecs, and frame rates (FPS).

Frame dimensions, display aspect ratios (DAR), and duration metrics.

Combined audio/video multiplex stream inspection.

Reporting (report_generator.py):

Consolidates diagnostic outputs into structured JSON format (reports/report.json).

2. Voice Cloning Studio

Zero-Shot Voice Cloning: Clones a target speaker from a reference recording (5–15 seconds of clean speech).

Text-to-Speech (TTS): Generates natural-sounding synthesized speech from arbitrary input text in the target voice.

Flexible Backends:

Free Cloud Backend: Zero-setup inference via Hugging Face (gradio_client).

Local Offline Backend: Fully local execution powered by XTTS-v2 / PyTorch.

Installation & Setup

Prerequisites

Python 3.10 to 3.12

Git

Clone the Repository

git clone https://github.com/ambika277/multimedia-analyzer.git
cd multimedia-analyzer


Usage Guide

A. Running the Multimedia Analyzer

Install requirements:

pip install -r requirements.txt


Run the analyzer:

python multimedia/multimedia_analyzer/main.py


Follow the on-screen prompts to inspect individual files or batch-scan a folder. Results are exported to reports/report.json.

B. Running Voice Cloning

Navigate to the voice-cloning directory:

cd voice-cloning


Create and activate a virtual environment:

Windows (Git Bash / PowerShell):

python -m venv .venv
source .venv/Scripts/activate
# or in PowerShell: .venv\Scripts\Activate.ps1


macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install gradio_client


Prepare reference audio:
Place a clear 5–15 second audio recording inside voice-cloning/samples/ (e.g., samples/sample.wav).

Run the script:

python app.py


Enter the audio path: samples/sample.wav

Enter the text you want the cloned voice to say.

Synthesized audio will be saved to voice-cloning/outputs/cloned_speech.wav.

License

This project is made available for academic and educational purposes under the MIT License.
