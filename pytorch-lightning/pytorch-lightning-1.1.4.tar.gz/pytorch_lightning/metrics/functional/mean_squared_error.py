# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Tuple

import torch

from pytorch_lightning.metrics.utils import _check_same_shape


def _mean_squared_error_update(preds: torch.Tensor, target: torch.Tensor) -> Tuple[torch.Tensor, int]:
    _check_same_shape(preds, target)
    sum_squared_error = torch.sum(torch.pow(preds - target, 2))
    n_obs = target.numel()
    return sum_squared_error, n_obs


def _mean_squared_error_compute(sum_squared_error: torch.Tensor, n_obs: int) -> torch.Tensor:
    return sum_squared_error / n_obs


def mean_squared_error(preds: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """
    Computes mean squared error

    Args:
        pred: estimated labels
        target: ground truth labels

    Return:
        Tensor with MSE

    Example:

        >>> x = torch.tensor([0., 1, 2, 3])
        >>> y = torch.tensor([0., 1, 2, 2])
        >>> mean_squared_error(x, y)
        tensor(0.2500)

    """
    sum_squared_error, n_obs = _mean_squared_error_update(preds, target)
    return _mean_squared_error_compute(sum_squared_error, n_obs)
