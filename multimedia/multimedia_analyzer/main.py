import sys

from file_utils import file_exists, get_file_type
from image_analyzer import analyze_image
from audio_analyzer import analyze_audio
from video_analyzer import analyze_video
from report_generator import save_report


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_exists(file_path):
        print("Error: File does not exist.")
        sys.exit(1)

    file_type = get_file_type(file_path)

    print(f"Detected file type: {file_type}")

    if file_type == "image":
        report = analyze_image(file_path)

    elif file_type == "audio":
        report = analyze_audio(file_path)

    elif file_type == "video":
        report = analyze_video(file_path)

    else:
        print("Error: Unsupported file type.")
        sys.exit(1)

    if report:
        save_report(report)


if __name__ == "__main__":
    main()