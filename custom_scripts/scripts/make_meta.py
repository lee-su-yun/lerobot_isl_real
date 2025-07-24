import json
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import os

def make_episode_jsonl(index, output_dir):

    parquet_file_path = f"/data/piper_grape0724/lerobot_5hz/data/chunk-{index // 50:03d}/episode_{index:06d}.parquet"

    file_path = Path(parquet_file_path)
    try:
        df = pd.read_parquet(file_path)
        length = len(df)
        episode = {
            "episode_index": index,
            "tasks": ["Pick the grape and put it in the basket."],
            "length": length
        }
        output_path = Path(output_dir) /"meta"/ "episodes.jsonl"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "a") as f:
            f.write(json.dumps(episode) + "\n")
        print(f"Saved episode {index} to {output_path}")
    except Exception as e:
        print(f"Failed to process index {index}: {e}")

def add_index_to_parquet(index, running_offset):
    parquet_file_path = f"/data/piper_grape0724/lerobot_5hz/data/chunk-{index // 50:03d}/episode_{index:06d}.parquet"
    df = pd.read_parquet(parquet_file_path)

    # df["index"] = range(running_offset, running_offset + len(df))
    # # if index < 600:
    # #     df["task_index"] = 2
    # # else:
    # #     df["task_index"] = 3
    # df.to_parquet(parquet_file_path, index=False)
    return len(df)  # return length to update running_offset


if __name__ == "__main__":
    #for i in tqdm(range(5)):
    total_frames, offset = 0, 0
    episodes_jsonl_path = "/data/piper_grape_0724/lerobot_5hz"
    for i in tqdm(range(600)):
        # make_episode_jsonl(i, episodes_jsonl_path)
        length = add_index_to_parquet(i, offset)
        offset += length
    print(f'total_frame is : {offset}')