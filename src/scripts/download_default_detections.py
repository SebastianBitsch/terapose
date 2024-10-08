import os

import hydra
from omegaconf import DictConfig, OmegaConf

from src.utils.logging import get_logger

# HACK: see: https://stackoverflow.com/a/76218591
import os
os.environ['CURL_CA_BUNDLE'] = ''

logger = get_logger(__name__)

def run_download(config: DictConfig) -> None:
    logger.info(f"Saving default detections to {config.data.test.dataloader.root_dir}/default_detections")

    download_cmd = f"huggingface-cli download bop-benchmark/datasets --include default_detections/* --local-dir {config.data.test.dataloader.root_dir} --repo-type=dataset"
    logger.info(f"Running {download_cmd}")
    os.system(download_cmd)
    logger.info("Default detections downloaded!")


@hydra.main(
    version_base=None,
    config_path="../../configs",
    config_name="test",
)
def download(cfg: DictConfig) -> None:
    OmegaConf.set_struct(cfg, False)
    run_download(cfg)


if __name__ == "__main__":
    download()
