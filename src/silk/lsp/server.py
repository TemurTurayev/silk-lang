"""
Silk Language Server

LSP server using pygls providing:
- Real-time diagnostics (parse/syntax errors)
- Autocompletion (keywords, builtins, medical functions)
- Hover documentation
- Document symbols (outline)
"""

from __future__ import annotations

import logging

from pygls.lsp.server import LanguageServer
from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
    TEXT_DOCUMENT_DOCUMENT_SYMBOL,
    TEXT_DOCUMENT_HOVER,
    CompletionList,
    CompletionOptions,
    CompletionParams,
    DidChangeTextDocumentParams,
    DidCloseTextDocumentParams,
    DidOpenTextDocumentParams,
    DidSaveTextDocumentParams,
    DocumentSymbolParams,
    Hover,
    HoverParams,
    MarkupContent,
    MarkupKind,
)

from .analyzer import analyze_document, get_word_at_position
from .completion_data import get_all_completions

logger = logging.getLogger("silk-lsp")


class SilkLanguageServer(LanguageServer):
    """Silk Language Server with document tracking."""

    def __init__(self) -> None:
        super().__init__("silk-language-server", "v0.2.0")
        self._docs: dict[str, str] = {}
        self._completions = get_all_completions()
        self._hover_index = _build_hover_index(self._completions)


def _build_hover_index(completions: list) -> dict[str, MarkupContent]:
    """Build a lookup dict from name -> hover documentation."""
    index: dict[str, MarkupContent] = {}
    for item in completions:
        if item.documentation and isinstance(item.documentation, MarkupContent):
            detail = item.detail or ""
            doc_value = item.documentation.value
            hover_text = f"**{item.label}**"
            if detail:
                hover_text += f"\n\n`{detail}`"
            hover_text += f"\n\n---\n\n{doc_value}"
            index[item.label] = MarkupContent(
                kind=MarkupKind.Markdown,
                value=hover_text,
            )
        elif item.detail:
            index[item.label] = MarkupContent(
                kind=MarkupKind.Markdown,
                value=f"**{item.label}** \u2014 {item.detail}",
            )
    return index


def create_server() -> SilkLanguageServer:
    """Create and configure the Silk language server."""
    server = SilkLanguageServer()

    # ─── Document Sync ─────────────────────────────────────

    @server.feature(TEXT_DOCUMENT_DID_OPEN)
    def did_open(params: DidOpenTextDocumentParams) -> None:
        uri = params.text_document.uri
        source = params.text_document.text
        server._docs[uri] = source
        _validate(server, uri, source)

    @server.feature(TEXT_DOCUMENT_DID_CHANGE)
    def did_change(params: DidChangeTextDocumentParams) -> None:
        uri = params.text_document.uri
        for change in params.content_changes:
            # Full sync: just take the latest text
            if hasattr(change, 'text'):
                server._docs[uri] = change.text
        source = server._docs.get(uri, "")
        _validate(server, uri, source)

    @server.feature(TEXT_DOCUMENT_DID_SAVE)
    def did_save(params: DidSaveTextDocumentParams) -> None:
        uri = params.text_document.uri
        source = server._docs.get(uri, "")
        _validate(server, uri, source)

    @server.feature(TEXT_DOCUMENT_DID_CLOSE)
    def did_close(params: DidCloseTextDocumentParams) -> None:
        uri = params.text_document.uri
        server._docs.pop(uri, None)
        # Clear diagnostics
        server.publish_diagnostics(uri, [])

    # ─── Completion ────────────────────────────────────────

    @server.feature(
        TEXT_DOCUMENT_COMPLETION,
        CompletionOptions(trigger_characters=[".", "(", ":"]),
    )
    def completions(params: CompletionParams) -> CompletionList:
        return CompletionList(
            is_incomplete=False,
            items=server._completions,
        )

    # ─── Hover ─────────────────────────────────────────────

    @server.feature(TEXT_DOCUMENT_HOVER)
    def hover(params: HoverParams) -> Hover | None:
        uri = params.text_document.uri
        source = server._docs.get(uri, "")
        line = params.position.line
        char = params.position.character

        word = get_word_at_position(source, line, char)
        if word is None:
            return None

        hover_content = server._hover_index.get(word)
        if hover_content is not None:
            return Hover(contents=hover_content)

        return None

    # ─── Document Symbols ──────────────────────────────────

    @server.feature(TEXT_DOCUMENT_DOCUMENT_SYMBOL)
    def document_symbols(params: DocumentSymbolParams) -> list:
        uri = params.text_document.uri
        source = server._docs.get(uri, "")
        _diagnostics, _ast, symbols = analyze_document(source, uri)
        return symbols

    return server


def _validate(server: SilkLanguageServer, uri: str, source: str) -> None:
    """Parse the document and publish diagnostics."""
    diagnostics, _ast, _symbols = analyze_document(source, uri)
    server.publish_diagnostics(uri, diagnostics)
