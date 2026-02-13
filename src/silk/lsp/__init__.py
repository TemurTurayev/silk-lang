"""
Silk Language Server Protocol (LSP) Implementation

Provides IDE features for the Silk programming language:
- Real-time diagnostics (syntax/parse errors)
- Autocompletion (keywords, builtins, medical functions)
- Hover documentation
- Document symbols
"""

from .server import create_server

__all__ = ["create_server"]
