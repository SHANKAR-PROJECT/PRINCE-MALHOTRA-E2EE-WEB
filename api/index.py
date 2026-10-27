import sys
from pathlib import Path

# Allow the Vercel Python function to import the Flask app from the project root.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app

__all__ = ["app"]
