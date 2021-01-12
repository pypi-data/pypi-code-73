#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#

from pinecone.functions import Function

from abc import abstractmethod
from typing import Dict, Union, Optional


class Engine(Function):

    """
    Generic interface for defining an engine
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError

    def get_stats(self) -> Dict[str, Union[int, float, str]]:
        return {'size': self.size()}

    @property
    def memory_request(self) -> int:
        return 1000

    @property
    def volume_request(self) -> Optional[int]:
        return 15
