# Multimedia Analyzer

A modular Python tool designed to inspect, analyze, and extract metadata and metrics from various media types (audio, image, and video files) and compile the results into structured reports.

---

## Features

* **Image Analysis (`image_analyzer.py`):** Inspects dimensions, color channels, formats, and metadata.
* **Audio Analysis (`audio_analyzer.py`):** Extracts sample rates, bitrates, audio channels, and duration metrics.
* **Video Analysis (`video_analyzer.py`):** Analyzes video resolution, framerate, codecs, and container details.
* **Automated Reporting (`report_generator.py`):** Aggregates findings into formatted JSON or summary files in the `reports/` directory.

---

## Project Structure

```text
multimedia-analyzer/
│
├── audio_analyzer.py       # Audio parsing routines
├── image_analyzer.py       # Image inspection tools
├── video_analyzer.py       # Video extraction logic
├── file_utils.py           # Shared file-handling helpers
├── report_generator.py     # Results compiler
├── main.py                 # Core CLI entry point
├── requirements.txt        # Project dependencies
└── reports/                # Output analysis files
