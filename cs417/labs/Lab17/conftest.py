<<<<<<< HEAD
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
=======
"""Path setup so tests can import from src/."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))
>>>>>>> main
