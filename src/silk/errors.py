"""
Silk Error Classes

All custom exceptions for the Silk language.
"""


class SilkError(Exception):
    """Base error for Silk language."""

    def __init__(self, message: str, line: int | None = None, col: int | None = None):
        self.message = message
        self.line = line
        self.col = col
        prefix = f"[line {line}]" if line else ""
        super().__init__(f"{prefix} {message}")


class LexerError(SilkError):
    """Error during tokenization."""
    pass


class ParseError(SilkError):
    """Error during parsing."""
    pass


class RuntimeError_(SilkError):
    """Error during execution."""
    pass


# Control flow signals (not actual errors)

class ReturnSignal(Exception):
    """Signal for function return."""

    def __init__(self, value):
        self.value = value


class BreakSignal(Exception):
    """Signal for loop break."""
    pass


class ContinueSignal(Exception):
    """Signal for loop continue."""
    pass
