import json
import pandas as pd
from pathlib import Path
from tqdm import tqdm

def make_episode_jsonl(index, output_dir):

    parquet_file_path = f"/data/piper_grape0626/lerobot_5hz/data/chunk-{index // 50:03d}/episode_{index:06d}.parquet"
    file_path = Path(parquet_file_path)
    try:
        df = pd.read_parquet(file_path)
        length = len(df)
        episode = {
            "episode_index": index,
            "tasks": ["Pick the grape and put it in the basket."],
            "length": length
        }
        output_path = Path(output_dir) / "episodes.jsonl"
        with open(output_path, "a") as f:
            f.write(json.dumps(episode) + "\n")
        print(f"Saved episode {index} to {output_path}")
    except Exception as e:
        print(f"Failed to process index {index}: {e}")
    return length

if __name__ == "__main__":
    #for i in tqdm(range(5)):
    total_frames = 0
    episodes_jsonl_path = "/data/piper_grape0626/lerobot_5hz"
    for i in tqdm(range(600)):
        total_frames += make_episode_jsonl(i, episodes_jsonl_path)
    print(f'total_frame is : {total_frames}')