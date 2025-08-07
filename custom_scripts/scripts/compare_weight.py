import logging
import time
from contextlib import nullcontext
from dataclasses import asdict
from pprint import pformat
from typing import Any
from collections import deque

import numpy as np
import torch
from termcolor import colored
from tqdm import tqdm
import matplotlib.pyplot as plt

from custom_scripts.common.utils.utils import load_buffer, get_current_action, plot_trajectory, pretty_plot

from lerobot.common.datasets.lerobot_dataset import LeRobotDatasetMetadata
from lerobot.common.datasets.factory import make_dataset
from lerobot.common.datasets.sampler import EpisodeAwareSampler
from lerobot.common.datasets.utils import cycle

from lerobot.common.policies.factory import make_policy
from lerobot.common.policies.pretrained import PreTrainedPolicy
from lerobot.common.policies.utils import get_device_from_parameters

from lerobot.common.utils.wandb_utils import WandBLogger
from lerobot.common.utils.logging_utils import AverageMeter, MetricsTracker
from lerobot.common.utils.random_utils import set_seed
from lerobot.common.utils.utils import (
    get_safe_torch_device,
    init_logging,
    format_big_number,
)

from lerobot.configs import parser
from custom_scripts.configs.eval_ours import EvalOursPipelineConfig


def evaluate_policy(
    eval_metrics: MetricsTracker,
    policy: PreTrainedPolicy,
    batch: Any,
    use_amp: bool = False,
    lock=None,
) -> tuple[MetricsTracker, dict]:
    start_time = time.perf_counter()
    device = get_device_from_parameters(policy)
    policy.eval()
    with torch.autocast(device_type=device.type) if use_amp else nullcontext():
        loss, output_dict = policy.forward(batch)
        # TODO(rcadene): policy.unnormalize_outputs(out_dict)

    eval_metrics.loss = loss.item()
    eval_metrics.update_s = time.perf_counter() - start_time
    return eval_metrics, output_dict


@parser.wrap()
def eval_main(cfg: EvalOursPipelineConfig):
    logging.info(pformat(asdict(cfg)))

    if cfg.wandb.enable and cfg.wandb.project:
        wandb_logger = WandBLogger(cfg)
    else:
        wandb_logger = None
        logging.info(colored("Logs will be saved locally.", "yellow", attrs=["bold"]))

    # Check device is available
    device = get_safe_torch_device(cfg.policy.device, log=True)
    torch.backends.cudnn.benchmark = True
    torch.backends.cuda.matmul.allow_tf32 = True
    set_seed(cfg.seed)

    logging.info(colored("Output dir:", "yellow", attrs=["bold"]) + f" {cfg.output_dir}")

    logging.info("Creating dataset")
    train_dataset_meta = LeRobotDatasetMetadata(
        cfg.train_dataset.repo_id, cfg.train_dataset.root, revision=cfg.train_dataset.revision
    )
    dataset = make_dataset(cfg)
    # x = dataset[0]['observation.images.exo']

    logging.info("Making policy.")

    policy = make_policy(
        cfg=cfg.policy,
        ds_meta=train_dataset_meta,
    )



if __name__ == "__main__":
    init_logging()
    eval_main()
