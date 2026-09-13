# Multimedia Analyzer

A comprehensive Python toolkit designed to parse, inspect, and analyze multimedia assets across different formats (images, audio, and video). It extracts deep metadata, verifies file integrity, evaluates technical encoding properties, and exports structured reports for analysis and archiving.

---

## Key Features

* **Image Analysis (`image_analyzer.py`):**
  * Detects dimensions (width, height), color mode (RGB, RGBA, Grayscale), and image format.
  * Inspects embedded EXIF metadata (camera model, orientation, timestamp, ISO).
  * Evaluates file compression and compression artifacts.

* **Audio Analysis (`audio_analyzer.py`):**
  * Extracts sample rate, channel count (mono/stereo/surround), bit depth, and bitrate.
  * Measures playback duration and identifies audio container/codec types (MP3, WAV, FLAC, AAC).
  * Inspects audio tags and stream headers.

* **Video Analysis (`video_analyzer.py`):**
  * Extracts container format, stream counts, video codecs, and frame rates (FPS).
  * Detects video dimensions, display aspect ratios, and total duration.
  * Analyzes interleaved audio and video stream properties.

* **File Utilities (`file_utils.py`):**
  * Validates file extensions, paths, and MIME types.
  * Manages safe directory traversal and file batch loading.

* **Report Generator (`report_generator.py`):**
  * Aggregates findings from individual analyzers into a cohesive output.
  * Automatically serializes data into structured JSON format (`reports/report.json`).

---

## Directory Architecture

```text
multimedia-analyzer/
├── audio_analyzer.py       # Audio parsing logic and metadata extraction
├── image_analyzer.py       # Image properties and EXIF tag reader
├── video_analyzer.py       # Video stream and container analyzer
├── file_utils.py           # Shared file-system helpers and validation
├── report_generator.py     # Results compiler and JSON formatter
├── main.py                 # CLI execution entry point
├── .gitignore              # Environment and binary exclusion rules
├── requirements.txt        # Package dependencies
└── reports/
    └── report.json         # Automated analysis output
