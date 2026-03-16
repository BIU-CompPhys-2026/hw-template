"""
conftest.py — adds repo root to sys.path so tests can import solution.py.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
