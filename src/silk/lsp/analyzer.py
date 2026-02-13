"""
Silk LSP Document Analyzer

Parses Silk source code and extracts diagnostics, symbols, and hover info.
"""

from __future__ import annotations

from lsprotocol.types import (
    Diagnostic,
    DiagnosticSeverity,
    DocumentSymbol,
    Position,
    Range,
    SymbolKind,
)

from ..lexer import Lexer
from ..parser import Parser
from ..errors import LexerError, ParseError


def analyze_document(source: str, uri: str) -> tuple[list[Diagnostic], list, list[DocumentSymbol]]:
    """
    Parse source code and return (diagnostics, ast_nodes, symbols).

    Returns:
        diagnostics: List of errors/warnings
        ast_nodes: Parsed AST statements (empty on error)
        symbols: Document symbols for outline
    """
    diagnostics: list[Diagnostic] = []
    ast_nodes: list = []
    symbols: list[DocumentSymbol] = []

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
    except LexerError as e:
        diagnostics.append(_error_to_diagnostic(e))
        return diagnostics, ast_nodes, symbols

    try:
        parser = Parser(tokens)
        program = parser.parse()
        ast_nodes = program.statements
    except ParseError as e:
        diagnostics.append(_error_to_diagnostic(e))
        return diagnostics, ast_nodes, symbols
    except Exception as e:
        line = getattr(e, 'line', None) or 1
        col = getattr(e, 'col', None) or 0
        diagnostics.append(Diagnostic(
            range=Range(
                start=Position(line=max(0, line - 1), character=max(0, col - 1)),
                end=Position(line=max(0, line - 1), character=max(0, col + 20)),
            ),
            message=str(e),
            severity=DiagnosticSeverity.Error,
            source="silk",
        ))
        return diagnostics, ast_nodes, symbols

    symbols = _extract_symbols(ast_nodes, source)
    return diagnostics, ast_nodes, symbols


def _error_to_diagnostic(e: LexerError | ParseError) -> Diagnostic:
    """Convert a Silk error to an LSP Diagnostic."""
    line = max(0, (e.line or 1) - 1)
    col = max(0, (e.col or 1) - 1)
    return Diagnostic(
        range=Range(
            start=Position(line=line, character=col),
            end=Position(line=line, character=col + 20),
        ),
        message=e.message,
        severity=DiagnosticSeverity.Error,
        source="silk",
    )


def _extract_symbols(statements: list, source: str) -> list[DocumentSymbol]:
    """Extract document symbols from AST for the outline view."""
    symbols: list[DocumentSymbol] = []
    lines = source.split('\n')

    for stmt in statements:
        symbol = _node_to_symbol(stmt, lines)
        if symbol is not None:
            symbols.append(symbol)

    return symbols


def _node_to_symbol(node, lines: list[str]) -> DocumentSymbol | None:
    """Convert an AST node to a DocumentSymbol if applicable."""
    node_type = type(node).__name__

    if node_type == 'FunctionDef':
        return _make_symbol(
            name=node.name,
            kind=SymbolKind.Function,
            line=_get_line(node),
            lines=lines,
            detail=_fn_detail(node),
            children=None,
        )

    if node_type == 'StructDef':
        field_symbols = [
            _make_symbol(
                name=f.name if hasattr(f, 'name') else str(f),
                kind=SymbolKind.Field,
                line=_get_line(node),
                lines=lines,
            )
            for f in (node.fields if hasattr(node, 'fields') else [])
        ]
        return _make_symbol(
            name=node.name,
            kind=SymbolKind.Struct,
            line=_get_line(node),
            lines=lines,
            children=field_symbols if field_symbols else None,
        )

    if node_type == 'EnumDef':
        variant_symbols = [
            _make_symbol(
                name=v.name if hasattr(v, 'name') else str(v),
                kind=SymbolKind.EnumMember,
                line=_get_line(node),
                lines=lines,
            )
            for v in (node.variants if hasattr(node, 'variants') else [])
        ]
        return _make_symbol(
            name=node.name,
            kind=SymbolKind.Enum,
            line=_get_line(node),
            lines=lines,
            children=variant_symbols if variant_symbols else None,
        )

    if node_type == 'ImplBlock':
        method_symbols = []
        target = node.target if hasattr(node, 'target') else "unknown"
        for method in (node.methods if hasattr(node, 'methods') else []):
            ms = _node_to_symbol(method, lines)
            if ms is not None:
                method_symbols.append(ms)
        return _make_symbol(
            name=f"impl {target}",
            kind=SymbolKind.Class,
            line=_get_line(node),
            lines=lines,
            children=method_symbols if method_symbols else None,
        )

    if node_type == 'InterfaceDef':
        return _make_symbol(
            name=node.name,
            kind=SymbolKind.Interface,
            line=_get_line(node),
            lines=lines,
        )

    if node_type == 'LetDeclaration':
        name = node.name if hasattr(node, 'name') else "?"
        return _make_symbol(
            name=name,
            kind=SymbolKind.Variable,
            line=_get_line(node),
            lines=lines,
        )

    if node_type == 'TestBlock':
        test_name = node.name if hasattr(node, 'name') else "test"
        return _make_symbol(
            name=f'test "{test_name}"',
            kind=SymbolKind.Function,
            line=_get_line(node),
            lines=lines,
            detail="test",
        )

    return None


def _get_line(node) -> int:
    """Get 0-based line number from an AST node."""
    if hasattr(node, 'line'):
        return max(0, node.line - 1)
    return 0


def _make_symbol(
    name: str,
    kind: SymbolKind,
    line: int,
    lines: list[str],
    detail: str | None = None,
    children: list[DocumentSymbol] | None = None,
) -> DocumentSymbol:
    """Create a DocumentSymbol with proper range."""
    line_len = len(lines[line]) if line < len(lines) else 0
    sym_range = Range(
        start=Position(line=line, character=0),
        end=Position(line=line, character=line_len),
    )
    return DocumentSymbol(
        name=name,
        kind=kind,
        range=sym_range,
        selection_range=sym_range,
        detail=detail,
        children=children,
    )


def _fn_detail(node) -> str:
    """Build a function detail string from AST node."""
    params = []
    if hasattr(node, 'params'):
        for p in node.params:
            if isinstance(p, tuple) and len(p) >= 2:
                name, type_hint = p[0], p[1]
                if type_hint:
                    params.append(f"{name}: {type_hint}")
                else:
                    params.append(str(name))
            else:
                params.append(str(p))

    ret = ""
    if hasattr(node, 'return_type') and node.return_type:
        ret = f" -> {node.return_type}"

    return f"fn({', '.join(params)}){ret}"


def get_word_at_position(source: str, line: int, character: int) -> str | None:
    """Get the word at a given position in the source code."""
    lines = source.split('\n')
    if line >= len(lines):
        return None

    text = lines[line]
    if character >= len(text):
        return None

    start = character
    while start > 0 and (text[start - 1].isalnum() or text[start - 1] == '_'):
        start -= 1

    end = character
    while end < len(text) and (text[end].isalnum() or text[end] == '_'):
        end += 1

    word = text[start:end]
    return word if word else None
