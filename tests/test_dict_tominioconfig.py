"""
Tests for dict .toMinIOConfig() method - MinIO config format.
"""

from silk.interpreter import Interpreter


class TestDictToMinIOConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMinIOConfig_basic(self):
        output = self._run('print({"port": 9000}.toMinIOConfig())')
        assert output[-1] == "port = 9000"

    def test_toMinIOConfig_string(self):
        output = self._run('print({"region": "us-east"}.toMinIOConfig())')
        assert output[-1] == "region = us-east"
