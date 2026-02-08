"""
Tests for dict .toEKSConfig() method - format as EKS config.
"""

from silk.interpreter import Interpreter


class TestDictToEKSConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEKSConfig_basic(self):
        output = self._run('print({"cluster": "main"}.toEKSConfig())')
        assert output[-1] == "cluster = main"

    def test_toEKSConfig_multi(self):
        output = self._run('print({"nodes": 3, "version": "1.28"}.toEKSConfig())')
        assert "version = 1.28" in output[-1]
