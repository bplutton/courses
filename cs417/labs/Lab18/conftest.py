"""
Pytest configuration — adds src/ to the import path.

This file lets pytest find your code in src/ when tests are in tests/.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
