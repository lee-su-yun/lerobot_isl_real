import os
import pandas as pd
from glob import glob
import numpy as np

# 기준 경로 설정
base_dir = "/home/sylee/codes/pick_grape/data"  # 여기에 chunk000~chunk009이 있는 상위 디렉토리 경로를 입력하세요

# 누적 데이터프레임 리스트
all_data = []

# chunk000 ~ chunk009 순회
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

# 원하는 컬럼
target_columns = ['action', 'observation.state', 'timestamp', 'frame_index', 'episode_index', 'task_index', 'index']

# 통계 계산
stats = {}
for col in target_columns:
    col_data = full_df[col]

    # 리스트나 배열이면 numpy 변환
    if isinstance(col_data.iloc[0], (list, np.ndarray)):
        col_array = np.stack(col_data)
        stats[col] = {
            'mean': np.mean(col_array, axis=0),
            'std': np.std(col_array, axis=0),
            'max': np.max(col_array, axis=0),
            'min': np.min(col_array, axis=0)
        }
    else:
        stats[col] = {
            'mean': col_data.mean(),
            'std': col_data.std(),
            'max': col_data.max(),
            'min': col_data.min()
        }

# 출력 예시
for col, s in stats.items():
    print(f"\nColumn: {col}")
    for stat_name, value in s.items():
        print(f"  {stat_name}: {value}")