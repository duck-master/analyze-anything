"""
Analyzes an arbitrary Python object.

Functions:
* invert_dict(some_dict): A helper function.
* analyze_anything(something): Analyzes an arbitrary Python object. Returns a dictionary.
"""
from pprint import pprint

def invert_dict(some_dict):
    """
    Helper function for analyze_something

    Args:
    * some_dict (dict): The dictionary {keys: values} to invert.

    Returns:
    * dict: The data from some_dict in the form {values: [keys]}.
    """
    result = {}
    for key, value in some_dict.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result

def analyze_anything(something):
    """
    Analyzes an arbitrary object of potentially unknown type and structure.

    Args:
    * something (any): An arbitrary Python object to analyze.

    Returns:
    * dict: A JSON-like object representing the result of the analysis.
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
    pprint(analyze_anything(analyze_anything))
