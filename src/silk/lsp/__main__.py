"""
Silk LSP Server Entry Point

Run with:  python -m silk.lsp
Or via:    silk-lsp (after pip install)
"""

import argparse
import logging

from .server import create_server


def main() -> None:
    parser = argparse.ArgumentParser(description="Silk Language Server")
    parser.add_argument(
        "--stdio", action="store_true", default=True,
        help="Use stdio transport (default)",
    )
    parser.add_argument(
        "--tcp", action="store_true",
        help="Use TCP transport",
    )
    parser.add_argument(
        "--host", default="127.0.0.1",
        help="TCP host (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port", type=int, default=2087,
        help="TCP port (default: 2087)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable verbose logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    server = create_server()

    if args.tcp:
        server.start_tcp(args.host, args.port)
    else:
        server.start_io()


if __name__ == "__main__":
    main()
