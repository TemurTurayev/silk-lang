"""
Silk Module Path Resolver

Resolves import paths to absolute file paths.
"""

from pathlib import Path


class ModuleNotFoundError(Exception):
    """Raised when a module cannot be found."""
    def __init__(self, path: str, searched: list[Path]):
        self.path = path
        self.searched = searched
        locations = ", ".join(str(p) for p in searched)
        super().__init__(f"Module '{path}' not found. Searched: {locations}")


class ModuleResolver:
    """Resolves import paths to filesystem paths."""

    def __init__(self, stdlib_dir: Path | None = None):
        if stdlib_dir is None:
            stdlib_dir = Path(__file__).parent.parent.parent / "stdlib"
        self.stdlib_dir = stdlib_dir

    def resolve(self, import_path: str, importing_file: Path) -> Path | None:
        """Resolve an import path to an absolute file path.

        Args:
            import_path: The path from the import statement (e.g. "silk/math", "./utils")
            importing_file: The file containing the import statement

        Returns:
            Absolute Path to the .silk file, or None for native modules

        Raises:
            ModuleNotFoundError: If module file cannot be found
        """
        importing_dir = importing_file.parent

        if import_path.startswith("silk/"):
            return self._resolve_stdlib(import_path, importing_file)
        elif import_path.startswith("./"):
            return self._resolve_relative(import_path[2:], importing_dir)
        else:
            return self._resolve_relative(import_path, importing_dir)

    def _resolve_stdlib(self, import_path: str, importing_file: Path) -> Path | None:
        """Resolve silk/ prefixed path to stdlib directory.

        Returns None if no file exists (signals native module).
        """
        # Strip silk/ prefix
        relative = import_path[5:]  # len("silk/") == 5
        candidate = self.stdlib_dir / f"{relative}.silk"
        if candidate.exists():
            return candidate
        # No file found — may be a native module
        return None

    def _resolve_relative(self, relative_path: str, base_dir: Path) -> Path:
        """Resolve a relative import path."""
        candidate = base_dir / f"{relative_path}.silk"
        if candidate.exists():
            return candidate
        raise ModuleNotFoundError(relative_path, [candidate])

    @staticmethod
    def default_alias(import_path: str) -> str:
        """Compute default alias from import path (last segment)."""
        # Strip ./ prefix if present
        path = import_path.lstrip("./")
        # Return last segment
        segments = path.split("/")
        return segments[-1]
