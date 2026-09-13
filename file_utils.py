import os


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".tiff",
    ".tif",
    ".webp",
    ".bmp",
}

AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a",
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".webm",
    ".flv",
}


def file_exists(file_path):
    return os.path.isfile(file_path)


def get_file_size(file_path):
    return os.path.getsize(file_path)


def get_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def get_file_type(file_path):
    extension = get_extension(file_path)

    if extension in IMAGE_EXTENSIONS:
        return "image"

    if extension in AUDIO_EXTENSIONS:
        return "audio"

    if extension in VIDEO_EXTENSIONS:
        return "video"

    return "unknown"