import os
from utils.frame_extractor import extract_frames

RAW_PATH = "data/raw_videos"
OUTPUT_PATH = "data/frames"

def process_videos():
    for label in ["real", "fake"]:
        folder = os.path.join(RAW_PATH, label)

        for video in os.listdir(folder):
            video_path = os.path.join(folder, video)

            print(f"Processing {video_path}")
            extract_frames(video_path, OUTPUT_PATH, label)

if __name__ == "__main__":
    process_videos()