from typing import Dict, Union
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def add(x: int, y: int) -> Dict[str, Union[str, int]]:
    try:
        result = x + y
        return {"operation": "addition", "result": result}
    except Exception as e:
        logging.error(f"Error in addition operation: {e}")
        return {"error": f"Error in addition operation: {e}"}

def subtract(x: int, y: int) -> Dict[str, Union[str, int]]:
    try:
        result = x - y
        return {"operation": "subtraction", "result": result}
    except Exception as e:
        logging.error(f"Error in subtraction operation: {e}")
        return {"error": f"Error in subtraction operation: {e}"}

def multiply(x: int, y: int) -> Dict[str, Union[str, int]]:
    try:
        result = x * y
        return {"operation": "multiplication", "result": result}
    except Exception as e:
        logging.error(f"Error in multiplication operation: {e}")
        return {"error": f"Error in multiplication operation: {e}"}

print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))
