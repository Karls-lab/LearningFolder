"""
A property is like a proxy between the private variables 
and the 'public' variable. When accessing name, it 
runs it through getters and setters that have certain 
safeguards. 
"""


class Color:
    def __init__(self, rgb_value:int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name:
            raise ValueError(f"Ivalid name {name!r}")
        self._name = name 

    def _set_name(self, name: str) -> None:
        if not name:
            raise ValueError(f"Invalid name {name!r}")
        self._name = name 

    def _get_name(self) -> str:
        return self._name 
    
    name = property(_get_name, _set_name)


c = Color(0xff0000, "bright red")
print("HERE")
print(c.name)
c.name = "red"
print(c.name)
c.name = ""
print(c.name)