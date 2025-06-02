import os
import pandas as pd
from glob import glob
import numpy as np

# 기준 경로 설정
base_path = "/data/piper_subtask_data/pick/train/data"  # 여기에 chunk000~chunk009이 있는 상위 디렉토리 경로를 입력하세요

# 누적 데이터프레임 리스트
all_data = []

# chunk000 ~ chunk009 순회
for i in range(10):
    chunk_dir = os.path.join(base_path, f'chunk{i:03d}')

    # 해당 chunk 안의 모든 parquet 파일 경로 가져오기
    parquet_files = sorted(glob(os.path.join(chunk_dir, '*.parquet')))

    for file in parquet_files:
        df = pd.read_parquet(file)
        all_data.append(df)

# 모든 데이터를 하나의 DataFrame으로 병합
merged_df = pd.concat(all_data, ignore_index=True)

# 원하는 컬럼
target_columns = ['action', 'observation.state', 'timestamp', 'frame_index', 'episode_index', 'task_index', 'index']

# 통계 계산
stats = {}
for col in target_columns:
    col_data = merged_df[col]

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