DEVICES=0,1,2,3,4,5
TORCH_DISTRIBUTED_BUCKET_CAP_MB=10

CUDA_VISIBLE_DEVICES=${DEVICES} \
  torchrun \
    --nproc_per_node=6 \
    ./train_pi0_ddp.py \
    --policy.path=/ckpt/pi0 \
    --use_ddp=true \
    --dataset.repo_id=/data/piper_subtask_data/pick/train_5hz_real \
    --dataset.root=/data/piper_subtask_data/pick/train_5hz_real \
    --wandb.enable=true \
    --output_dir=/result/piper_subtask/pi0_test \
    --job_name=pi0_ddp_piper_pick \
    --wandb.disable_artifact=true \
    --batch_size=6 \
    --num_workers=16 \
    --log_freq=10 \
    --save_freq=10000 \
    --steps=40000