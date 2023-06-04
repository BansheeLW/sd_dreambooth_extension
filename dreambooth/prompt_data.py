import json
from dataclasses import dataclass, asdict
from typing import Union, List, Tuple
import copy

@dataclass
class PromptData:
    prompt:str = ""
    prompt_tokens: Union[List[str], None] = None
    negative_prompt:str = ""
    instance_token: str = ""
    class_token: str = ""
    src_image: str = ""
    steps:int = 60
    scale:float = 7.5
    out_dir:str = ""
    seed:int = -1
    resolution: Tuple[int, int] = (512, 512)
    concept_index: int = 0

    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)

    @property
    def json(self):
        """
        get the json formated string
        """
        return json.dumps(self.__dict__)

    def __deepcopy__(self, pd):
        cls = self.__class__
        result = cls.__new__(cls)
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, pd))
        return result
