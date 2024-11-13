"""
To analyze stuff
"""
from pprint import pprint

def invert_dict(some_dict):
    """
    Helper function for analyze_something
    """
    result = {}
    for k, v in some_dict.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result

def analyze_anything(something):
    """
    Analyzes an arbitrary object of potentially unknown type and structure
    """
    return {
        "type": type(something).__name__,
        "str": str(something)[:100],
        "repr": repr(something)[:100],
        "dir": invert_dict({
            k: type(getattr(something, k)).__name__
            for k in dir(something)
        })
    }

if __name__ == "__main__":
    # to show this function off, let's use it to analyze itself!
    pprint(analyze_something(analyze_something))
