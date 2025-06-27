import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

data_dir2 = Path("/data/piper_grape0626/lerobot_5hz/data/chunk-000/episode_000000.parquet")
data_dir1 = Path("/data/piper_grape0626/lerobot/data/chunk-000/episode_000000.parquet")
df2 = pd.read_parquet(data_dir2)
df = pd.read_parquet(data_dir1)

pd_xyz = pd.DataFrame(df["observation.state"].apply(lambda x: x[0][:3]).tolist(), columns=["x", "y", "z"])

# df2: [...] 구조 → x[:3]
pd2_xyz = pd.DataFrame(df2["observation.state"].apply(lambda x: x[:3]).tolist(), columns=["x", "y", "z"])

# --- Plot ---
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
dims = ["x", "y", "z"]

for i, dim in enumerate(dims):
    axes[i].plot(range(len(pd_xyz)), pd_xyz[dim], label=f"{dim} (df: line)", color="blue")
    axes[i].scatter([j * 6 for j in range(len(pd2_xyz))], pd2_xyz[dim], label=f"{dim} (df2: dots)", color="red", s=10)
    axes[i].set_ylabel(dim)
    axes[i].legend()
    axes[i].grid(True)

axes[-1].set_xlabel("Frame Index")
plt.suptitle("observation.state ")
plt.tight_layout()
plt.show()