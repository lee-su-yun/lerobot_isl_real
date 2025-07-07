
import pandas as pd
from pathlib import Path

for j in range(12):
    data_dir = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/data/chunk-{j:03d}")
    save_data_dir = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/data/chunk-{j+12:03d}")
    for i in range(50):
        filename = f"episode_{i+50*j:06d}.parquet"
        file_path = data_dir / filename
        # Load
        df = pd.read_parquet(file_path)
        # Modify columns
        new_filename = f"episode_{i + 50 * (j + 12):06d}.parquet"
        df.to_parquet(save_data_dir / new_filename)

