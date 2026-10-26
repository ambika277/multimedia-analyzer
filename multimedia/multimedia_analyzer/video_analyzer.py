import json
import os
import subprocess
import sys


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

    seconds = float(seconds)

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_metadata(video_path):

    command = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        video_path,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return json.loads(result.stdout)


def analyze_video(video_path):

    if not os.path.isfile(video_path):
        print("Error: File does not exist.")
        return None

    try:
        data = get_metadata(video_path)

        format_data = data.get("format", {})
        streams = data.get("streams", [])

        video_stream = None
        audio_stream = None

        for stream in streams:
            if stream.get("codec_type") == "video" and video_stream is None:
                video_stream = stream

            elif stream.get("codec_type") == "audio" and audio_stream is None:
                audio_stream = stream

        metadata = {
            "type": "video",
            "file_name": os.path.basename(video_path),
            "file_size": format_file_size(os.path.getsize(video_path)),
            "container": format_data.get("format_name", "Unknown"),
            "duration": format_duration(format_data.get("duration")),
            "video": {},
            "audio": {},
            "metadata": format_data.get("tags", {}),
        }

        if video_stream:
            width = video_stream.get("width")
            height = video_stream.get("height")

            fps = video_stream.get("r_frame_rate", "Unknown")

            if "/" in fps:
                numerator, denominator = fps.split("/")

                if float(denominator) != 0:
                    fps = round(
                        float(numerator) / float(denominator),
                        2
                    )

            bitrate = video_stream.get("bit_rate")

            metadata["video"] = {
                "resolution": f"{width} x {height}",
                "frame_rate": f"{fps} FPS",
                "bit_rate": (
                    f"{int(bitrate) // 1000} kbps"
                    if bitrate
                    else "Unknown"
                ),
                "codec": video_stream.get(
                    "codec_name",
                    "Unknown"
                ),
            }

        if audio_stream:
            bitrate = audio_stream.get("bit_rate")

            metadata["audio"] = {
                "codec": audio_stream.get(
                    "codec_name",
                    "Unknown"
                ),
                "channels": audio_stream.get(
                    "channels",
                    "Unknown"
                ),
                "sampling_rate": (
                    f"{audio_stream.get('sample_rate')} Hz"
                    if audio_stream.get("sample_rate")
                    else "Unknown"
                ),
                "bit_rate": (
                    f"{int(bitrate) // 1000} kbps"
                    if bitrate
                    else "Unknown"
                ),
            }

        print("\n================================")
        print("VIDEO METADATA REPORT")
        print("================================")

        print(f"\nFile Name       : {metadata['file_name']}")
        print(f"File Size       : {metadata['file_size']}")
        print(f"Container       : {metadata['container']}")
        print(f"Duration        : {metadata['duration']}")

        print("\nVIDEO")
        print("--------------------------------")

        for key, value in metadata["video"].items():
            label = key.replace("_", " ").title()
            print(f"{label:<16}: {value}")

        print("\nAUDIO")
        print("--------------------------------")

        for key, value in metadata["audio"].items():
            label = key.replace("_", " ").title()
            print(f"{label:<16}: {value}")

        print("\nMETADATA")
        print("--------------------------------")

        if metadata["metadata"]:
            for key, value in metadata["metadata"].items():
                print(f"{key:<20}: {value}")
        else:
            print("No metadata found.")

        return metadata

    except FileNotFoundError:
        print("Error: ffprobe was not found.")
        print("Please check your FFmpeg installation.")
        return None

    except Exception as error:
        print(f"Error analyzing video: {error}")
        return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python video_analyzer.py <video_path>")
        sys.exit(1)

    analyze_video(sys.argv[1])