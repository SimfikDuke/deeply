# Deeply - Make your dataclasses more functional  

Using this package you can do a deep conversion of your dataclass to a dictionary and initialize it from dict.  

###  Getting it  
  
To download deeply, either fork this github repo or simply use PyPI via pip.  
```sh
$ pip install deeply
```
  
## Usage  

1 - Import  
```python
from deeply import Deeply
from dataclasses import dataclass
```
  
2 - Define your data classes with the following inheritance:  
```python
@dataclass
class A(Deeply):
    a1: int
    a2: int


@dataclass
class B(Deeply):
    b1: str
    b2: str

@dataclass
class C(Deeply):
    a: A
    b: B

```
  
3 - Create an instance of the class and you can already use it:  
```python
c = C(A(1, 2), B('foo', 'bar'))

c.to_web()
# {'a': {'a1': 1, 'a2': 2}, 'b': {'b1': 'foo', 'b2': 'bar'}}

```
  
4 - You can also initialize your class from a dictionary:  
  
```python
c = C.init_from_dict({
    'a': {
        'a1': 1,
        'a2': 2
    }, 
    'b': {
        'b1': 'foo',
        'b2': 'bar'
    }
})

# C(a=A(a1=1, a2=2), b=B(b1='foo', b2='bar'))
```
  
5 - And finally: you can set your own conversion rules in deep dict.  
  
```python
Deeply.rules: List[Tuple[Callable[[T], bool], Callable[[T], Any]]] = [
        (lambda obj: hasattr(obj, 'isoformat'), lambda obj: obj.isoformat()),
    ]

```