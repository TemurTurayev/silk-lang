#!/usr/bin/env python3
"""
Silk CLI - Legacy wrapper.

The canonical CLI module is now at src/silk/cli.py.
This file is kept for backward compatibility with direct execution:
    python cli/silk_cli.py
"""

import sys
import os

# Add src to path so 'silk' package is importable when running directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.cli import main

if __name__ == '__main__':
    main()
