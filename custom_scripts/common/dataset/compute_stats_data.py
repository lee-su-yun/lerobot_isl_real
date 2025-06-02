import pandas as pd
import numpy as np
import os
import json
from tqdm import tqdm

base_dir = "/data/piper_subtask_data/pick/train/data"
columns = ['action', 'observation.state', 'timestamp', 'frame_index', 'episode_index', 'task_index', 'index']
vector_columns = ['action', 'observation.state']
stats = {col: {} for col in columns}
dfs = []

# 모든 parquet 파일 읽기
for chunk_id in range(10):
    chunk_path = os.path.join(base_dir, f"chunk-{chunk_id:03d}")
    for ep_id in range(20):
        file_path = os.path.join(chunk_path, f"episode_{chunk_id * 20 + ep_id:06d}.parquet")
        df = pd.read_parquet(file_path)
        dfs.append(df)

# 전체 결합
full_df = pd.concat(dfs, ignore_index=True)

# 통계 계산
for col in columns:
    if col in vector_columns:
        try:
            # 먼저 리스트를 배열로 변환
            array_list = [np.array(v, dtype=np.float32) for v in full_df[col].tolist()]
            arr = np.stack(array_list)  # shape (N, D)

            stats[col] = {
                "mean": np.mean(arr, axis=0).tolist(),
                "std": np.std(arr, axis=0).tolist(),
                "max": np.max(arr, axis=0).tolist(),
                "min": np.min(arr, axis=0).tolist(),
            }
        except Exception as e:
            print(f"Error processing {col}: {e}")
    else:
        series = full_df[col].astype(float)
        stats[col] = {
            "mean": float(series.mean()),
            "std": float(series.std()),
            "max": float(series.max()),
            "min": float(series.min()),
        }

# 결과 출력
print(json.dumps(stats, indent=2))