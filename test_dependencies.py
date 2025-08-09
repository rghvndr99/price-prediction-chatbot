#!/usr/bin/env python3

try:
    import numpy as np
    print("✓ numpy is available")
    print(f"numpy version: {np.__version__}")
except ImportError as e:
    print(f"✗ numpy is not available: {e}")

try:
    import json
    print("✓ json is available (built-in)")
except ImportError as e:
    print(f"✗ json is not available: {e}")

try:
    import os
    print("✓ os is available (built-in)")
except ImportError as e:
    print(f"✗ os is not available: {e}")

try:
    import pickle
    print("✓ pickle is available (built-in)")
except ImportError as e:
    print(f"✗ pickle is not available: {e}")

print("\nAll dependencies for util.py:")
print("- json: built-in Python module")
print("- os: built-in Python module") 
print("- pickle: built-in Python module")
print("- numpy: external dependency (needs to be installed)")
