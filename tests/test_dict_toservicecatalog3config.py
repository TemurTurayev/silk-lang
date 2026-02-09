"""
Tests for dict .toServiceCatalog3Config() method - format dict as ServiceCatalog3 config.
"""

from silk.interpreter import Interpreter


class TestDictToServiceCatalog3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toServiceCatalog3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toServiceCatalog3Config())')
        assert output[-1] == "host = localhost"

    def test_toServiceCatalog3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toServiceCatalog3Config())')
        assert output[-1] == "host = localhost\nport = 443"
