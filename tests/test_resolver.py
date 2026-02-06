"""Tests for module path resolution."""

import pytest
from pathlib import Path
from silk.resolver import ModuleResolver, ModuleNotFoundError


class TestModuleResolver:
    """Test module path resolution."""

    @pytest.fixture
    def resolver(self, tmp_path):
        """Create resolver with a temp stdlib dir."""
        stdlib = tmp_path / "stdlib"
        stdlib.mkdir()
        return ModuleResolver(stdlib_dir=stdlib)

    def test_relative_path_resolves(self, resolver, tmp_path):
        """./utils resolves relative to the importing file."""
        # Create the target module
        utils_file = tmp_path / "utils.silk"
        utils_file.write_text("fn helper() { return 1 }")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("./utils", importing_file)
        assert result == utils_file

    def test_relative_path_with_subdirectory(self, resolver, tmp_path):
        """./lib/geometry resolves to subdir."""
        lib_dir = tmp_path / "lib"
        lib_dir.mkdir()
        geo_file = lib_dir / "geometry.silk"
        geo_file.write_text("struct Circle { radius: float }")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("./lib/geometry", importing_file)
        assert result == geo_file

    def test_silk_prefix_resolves_to_stdlib(self, resolver, tmp_path):
        """silk/math resolves to stdlib directory."""
        math_file = resolver.stdlib_dir / "math.silk"
        math_file.write_text("let pi = 3.14159")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("silk/math", importing_file)
        assert result == math_file

    def test_silk_prefix_deep_path(self, resolver, tmp_path):
        """silk/medical/dosing resolves into stdlib subdirs."""
        medical_dir = resolver.stdlib_dir / "medical"
        medical_dir.mkdir()
        dosing_file = medical_dir / "dosing.silk"
        dosing_file.write_text("fn dose() { return 0 }")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("silk/medical/dosing", importing_file)
        assert result == dosing_file

    def test_bare_name_resolves_relative(self, resolver, tmp_path):
        """Bare name (no prefix) resolves relative to importing file."""
        helpers_file = tmp_path / "helpers.silk"
        helpers_file.write_text("fn h() { return 1 }")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("helpers", importing_file)
        assert result == helpers_file

    def test_missing_module_raises_error(self, resolver, tmp_path):
        """Nonexistent module raises ModuleNotFoundError."""
        importing_file = tmp_path / "main.silk"
        with pytest.raises(ModuleNotFoundError):
            resolver.resolve("./nonexistent", importing_file)

    def test_silk_extension_auto_appended(self, resolver, tmp_path):
        """Extension .silk is added automatically."""
        utils_file = tmp_path / "utils.silk"
        utils_file.write_text("")

        importing_file = tmp_path / "main.silk"
        result = resolver.resolve("./utils", importing_file)
        assert result.suffix == ".silk"

    def test_default_alias_last_segment(self):
        """Default alias is the last path segment."""
        assert ModuleResolver.default_alias("silk/math") == "math"
        assert ModuleResolver.default_alias("silk/medical/pediatrics") == "pediatrics"
        assert ModuleResolver.default_alias("./utils") == "utils"
        assert ModuleResolver.default_alias("./lib/geometry") == "geometry"
        assert ModuleResolver.default_alias("helpers") == "helpers"

    def test_native_module_returns_none(self, resolver, tmp_path):
        """silk/ path with no file returns None (native module)."""
        importing_file = tmp_path / "main.silk"
        # silk/math with no stdlib file → None (handled as native)
        result = resolver.resolve("silk/math", importing_file)
        assert result is None
