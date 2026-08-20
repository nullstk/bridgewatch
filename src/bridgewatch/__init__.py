"""BridgeWatch: Tracks bridge transactions and reports confirmation progress across chains."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]