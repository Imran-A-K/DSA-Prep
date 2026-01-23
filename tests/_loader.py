import os
import importlib

def load_func(func_name: str):
    module_name = os.getenv("DSA_SOLUTION_MODULE")
    if not module_name:
        raise RuntimeError(
            "DSA_SOLUTION_MODULE is not set. "
            "Run via: python run.py <test_file.py> <solution_file.py>"
        )
    mod = importlib.import_module(module_name)
    if not hasattr(mod, func_name):
        raise AttributeError(f"Module '{module_name}' does not define function '{func_name}'")
    return getattr(mod, func_name)