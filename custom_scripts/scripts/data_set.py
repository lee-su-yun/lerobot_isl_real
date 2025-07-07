
import pandas as pd
from pathlib import Path
import shutil

# for j in range(12):
#     data_dir = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/data/chunk-{j:03d}")
#     save_data_dir = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/data/chunk-{j+12:03d}")
#     for i in range(50):
#         filename = f"episode_{i+50*j:06d}.parquet"
#         file_path = data_dir / filename
#         # Load
#         df = pd.read_parquet(file_path)
#         # Modify columns
#         new_filename = f"episode_{i + 50 * (j + 12):06d}.parquet"
#         df.to_parquet(save_data_dir / new_filename)


for j in range(12):
    data_dir_exo = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j:03d}/observation.images.exo")
    data_dir_table = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j:03d}/observation.images.table")
    data_dir_wrist = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j:03d}/observation.images.wrist")

    save_data_dir_exo = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j+12:03d}/observation.images.exo")
    save_data_dir_table = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j+12:03d}/observation.images.table")
    save_data_dir_wrist = Path(f"/data/piper_grape0626_multiview/lerobot_5hz/videos/chunk-{j+12:03d}/observation.images.wrist")
    for i in range(50):
        global_index = i + 50 * j
        new_index = i + 50 * (j + 12)
        for cam, src_dir, dst_dir in zip(
                ["exo", "table", "wrist"],
                [data_dir_exo, data_dir_table, data_dir_wrist],
                [save_data_dir_exo, save_data_dir_table, save_data_dir_wrist]
        ):
            filename = f"episode_{global_index:06d}.mp4"
            new_filename = f"episode_{new_index:06d}.mp4"
            src_file = src_dir / filename
            dst_file = dst_dir / new_filename

            if src_file.exists():
                shutil.copy2(src_file, dst_file)
            else:
                print(f"Warning: {src_file} not found.")
