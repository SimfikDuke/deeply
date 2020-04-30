from typing import Iterable, Dict, Any, Callable, Tuple, Optional, TypeVar, Type, List
import dacite

T = TypeVar('T')


class Deeply:

    rules: List[Tuple[Callable[[T], bool], Callable[[T], Any]]] = [
        (lambda obj: hasattr(obj, 'isoformat'), lambda obj: obj.isoformat()),
    ]

    @classmethod
    def __deep_dict(cls, obj: T, rules: List[Tuple[Callable[[T], bool], Callable[[T], Any]]]):
        if hasattr(obj, '__dict__'):
            return {k: cls.__deep_dict(v, rules) for k, v in obj.__dict__.items()}
        elif isinstance(obj, Dict):
            return {k: cls.__deep_dict(v, rules) for k, v in obj.items()}
        elif isinstance(obj, Iterable) and not isinstance(obj, str):
            return [cls.__deep_dict(v, rules) for v in obj]
        for clause, decision in rules:
            if clause(obj):
                return decision(obj)
        return obj

    @property
    def __deep_dict__(self) -> Dict[str, Any]:
        return self.__deep_dict(self, self.rules)

    def to_web(self) -> Dict[str, Any]:
        return self.__deep_dict__

    @classmethod
    def init_from_dict(cls: Type[T], dict_: Dict[str, Any], config: Optional['dacite.Config'] = None) -> T:
        if config is None:
            config = dacite.Config(check_types=False)
        return dacite.from_dict(cls, dict_, config)
