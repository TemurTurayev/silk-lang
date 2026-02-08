"""
Tests for dict .toServiceCatalogConfig() method - format as Service Catalog config.
"""

from silk.interpreter import Interpreter


class TestDictToServiceCatalogConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toServiceCatalogConfig_basic(self):
        output = self._run('print({"portfolio": "data-products"}.toServiceCatalogConfig())')
        assert output[-1] == "portfolio = data-products"

    def test_toServiceCatalogConfig_multi(self):
        output = self._run('print({"owner": "platform", "type": "product"}.toServiceCatalogConfig())')
        assert "owner = platform" in output[-1]
