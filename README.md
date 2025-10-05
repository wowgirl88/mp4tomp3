```markdown
# MP4 to MP3 Converter

A simple Python script that converts MP4 video files to MP3 audio files using FFmpeg.

## Features

- Converts MP4 files to MP3 format
- Customizable audio bitrate
- Automatic output filename generation
- Error handling and validation

## Requirements

- Python 3.x
- FFmpeg installed and available in system PATH

### Installing FFmpeg

**Windows:**
- Download from https://ffmpeg.org/download.html
- Add to system PATH or place ffmpeg.exe in the same directory as the script

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

### Command Line

```bash
python main.py input_video.mp4
```

This will create `input_video.mp3` in the same directory.

### Function Call

```python
from converter import convert_mp4_to_mp3_ffmpeg

# Basic usage
convert_mp4_to_mp3_ffmpeg("video.mp4")

# Custom output filename and bitrate
convert_mp4_to_mp3_ffmpeg(
    "video.mp4", 
    "audio.mp3", 
    bitrate="256k"
)
```

## Parameters

- `mp4_file` (required): Path to input MP4 file
- `mp3_file` (optional): Path to output MP3 file. If not provided, uses the same name as input with .mp3 extension
- `bitrate` (optional): Audio bitrate (default: "192k"). Common values: "128k", "192k", "256k", "320k"

## Error Handling

The script handles various error scenarios:
- FFmpeg not found in PATH
- Input file not found or inaccessible
- FFmpeg conversion failures
- General exceptions

## License

This script is provided as-is for educational and personal use.
```
