from typing import Dict

def add(x: int, y: int) -> Dict[str, int]:
    result = x + y
    return {"sum": result}

def subtract(x: int, y: int) -> Dict[str, int]:
    result = x - y
    return {"difference": result}

def multiply(x: int, y: int) -> Dict[str, int]:
    result = x * y
    return {"product": result}

print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))
