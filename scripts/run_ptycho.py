import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import hydra
from omegaconf import DictConfig
from vlab_bench.dfo import DerivativeFreeOptimization

def run(config: DictConfig):
    assert config.dims > 0
    assert config.num_samples > 0

    dfo = DerivativeFreeOptimization(
            dfo_method=config.method,
            func=config.func,
            dims=config.dims,
            num_samples=config.num_samples,
            surrogate=None,
            num_init_samples=config.init_samples,
            dfo_method_args=config.dfo_method_args,
            func_args=config.ptycho,
    )

    dfo.run()

@hydra.main(version_base="1.3", config_path="conf", config_name="run_ptycho.yaml")
def main(config: DictConfig):
    run(config)

if __name__ == "__main__":
    main()