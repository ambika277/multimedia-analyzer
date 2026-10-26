# Multimedia Projects

A collection of Python-based multimedia applications for analyzing media files, experimenting with voice cloning, and enhancing images.

## Projects

### 1. Multimedia Analyzer
A Python application for analyzing multimedia files and extracting useful information.

**Features**
- Multimedia file analysis
- Metadata inspection
- Organized analysis results

**Folder:** `multimedia/`

### 2. Voice Cloning
A project exploring voice cloning and audio processing using Python.

**Folder:** `voice-cloning/`

### 3. Image Enhancement
A web-based image enhancement application built with Streamlit and Pillow. Upload an image, adjust its appearance, apply filters, and download the result.

**Features**
- Upload and preview images
- Adjust brightness, contrast, sharpness, and saturation
- Apply grayscale, sepia, blur, smooth, detail, and edge-enhancement effects
- Rotate and resize images
- Download enhanced images in PNG or JPEG format

**Technologies:** Python, Streamlit, Pillow

**Folder:** `image-enhancement/`

## Technologies Used

- Python
- Streamlit
- Pillow
- Multimedia and image-processing libraries

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ambika277/multimedia-analyzer.git
cd multimedia-analyzer
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
```

Activate it in Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

### 3. Run Image Enhancement

```bash
cd image-enhancement
pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## Repository Structure

```text
multimedia-analyzer/
├── multimedia/
├── voice-cloning/
├── image-enhancement/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── .gitignore
└── README.md
```

## Purpose

This repository brings together multimedia-related Python projects for learning, experimentation, and practical application development.

## Author

**Ambika**

