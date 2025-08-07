DEVICES=3,4
TORCH_DISTRIBUTED_BUCKET_CAP_MB=10

CUDA_VISIBLE_DEVICES=${DEVICES} \
  torchrun \
    --master-port 29600 \
    --nproc_per_node=2 \
    ./train_pi0_ddp.py \
    --policy.path=/ckpt/pi0 \
    --use_ddp=true \
    --dataset.repo_id=/data/piper_corn0724_0.6k/lerobot_5hz \
    --dataset.root=/data/piper_corn0724_0.6k/lerobot_5hz \
    --wandb.enable=true \
    --output_dir=/result/pi0_20250804_piper_pickcorn_with_grape_ep600_expert_only \
    --job_name=pi0_20250804_piper_pickcorn_with_grape_ep600_expert_only \
    --wandb.disable_artifact=true \
    --batch_size=9 \
    --num_workers=16 \
    --log_freq=10 \
    --save_freq=10000 \
    --steps=40000