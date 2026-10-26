import os
import sys

from mutagen import File


SUPPORTED_FORMATS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a",
}


def format_file_size(size):
    if size < 1024:
        return f"{size} B"

    if size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"

    if size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"

    return f"{size / (1024 ** 3):.2f} GB"


def format_duration(seconds):
    if seconds is None:
        return "Unknown"

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return f"{minutes:02d}:{seconds:02d}"


def analyze_audio(audio_path):

    if not os.path.isfile(audio_path):
        print("Error: File does not exist.")
        return None

    extension = os.path.splitext(audio_path)[1].lower()

    if extension not in SUPPORTED_FORMATS:
        print("Error: Unsupported audio format.")
        return None

    try:
        audio = File(audio_path)

        if audio is None:
            print("Error: Could not read audio file.")
            return None

        info = audio.info

        duration = getattr(info, "length", None)
        bitrate = getattr(info, "bitrate", None)
        sample_rate = getattr(info, "sample_rate", None)
        channels = getattr(info, "channels", None)

        metadata = {
            "type": "audio",
            "file_name": os.path.basename(audio_path),
            "file_size": format_file_size(os.path.getsize(audio_path)),
            "format": extension.replace(".", "").upper(),
            "duration": format_duration(duration),
            "bitrate": f"{bitrate // 1000} kbps" if bitrate else "Unknown",
            "sample_rate": f"{sample_rate} Hz" if sample_rate else "Unknown",
            "channels": channels if channels else "Unknown",
            "tags": {},
        }

        if audio.tags:
            for key, value in audio.tags.items():
                metadata["tags"][str(key)] = str(value)

        print("\n================================")
        print("AUDIO METADATA REPORT")
        print("================================")

        print(f"\nFile Name       : {metadata['file_name']}")
        print(f"File Size       : {metadata['file_size']}")
        print(f"Format          : {metadata['format']}")
        print(f"Duration        : {metadata['duration']}")

        print("\nAUDIO")
        print("--------------------------------")
        print(f"Codec/Format    : {metadata['format']}")
        print(f"Channels        : {metadata['channels']}")
        print(f"Sampling Rate   : {metadata['sample_rate']}")
        print(f"Bit Rate        : {metadata['bitrate']}")

        print("\nMETADATA")
        print("--------------------------------")

        if metadata["tags"]:
            for key, value in metadata["tags"].items():
                print(f"{key:<20}: {value}")
        else:
            print("No tags found.")

        return metadata

    except Exception as error:
        print(f"Error analyzing audio: {error}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio_analyzer.py <audio_path>")
        sys.exit(1)

    analyze_audio(sys.argv[1])