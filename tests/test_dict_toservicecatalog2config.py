"""
Tests for dict .toServiceCatalog2Config() method - format as ServiceCatalog v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToServiceCatalog2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toServiceCatalog2Config_basic(self):
        output = self._run('print({"portfolio": "infra"}.toServiceCatalog2Config())')
        assert output[-1] == "portfolio = infra"

    def test_toServiceCatalog2Config_multi(self):
        output = self._run('print({"portfolio": "infra", "product": "vpc"}.toServiceCatalog2Config())')
        assert output[-1] == "portfolio = infra\nproduct = vpc"
