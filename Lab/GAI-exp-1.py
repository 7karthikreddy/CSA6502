import sys
print(sys.version)

import sys

try:
    import numpy as np
    print("NumPy Version:", np.__version__)
except ImportError:
    print("NumPy is not installed.")

try:
    import pandas as pd
    print("Pandas Version:", pd.__version__)
except ImportError:
    print("Pandas is not installed.")

try:
    import matplotlib
    print("Matplotlib Version:", matplotlib.__version__)
except ImportError:
    print("Matplotlib is not installed.")

try:
    import sklearn
    print("Scikit-learn Version:", sklearn.__version__)
except ImportError:
    print("Scikit-learn is not installed.")

print("Python Version:", sys.version)
print("Verification Completed.")
