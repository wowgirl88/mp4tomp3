import subprocess
import os
import sys

def convert_mp4_to_mp3_ffmpeg(mp4_file, mp3_file=None, bitrate="192k"):
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error: ffmpeg not in PATH")
            return False
        
        if mp3_file is None:
            base_name = os.path.splitext(mp4_file)[0]
            mp3_file = base_name + '.mp3'
        
        command = [
            "ffmpeg",
            "-i", mp4_file,
            "-vn",         
            "-acodec", "mp3",
            "-ab", bitrate,
            "-y",
            mp3_file
        ]
        
        subprocess.run(command, check=True)
        print(f"[done] {mp3_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg error: {e}")
        return False
    except Exception as e:
        print(f"error: {e}")
        return False

if __name__ == "__main__":
    input_file = sys.argv[1]
    convert_mp4_to_mp3_ffmpeg(input_file)
