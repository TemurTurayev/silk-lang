"""
Tests for dict .toELBConfig() method - format as AWS Elastic Load Balancer config.
"""

from silk.interpreter import Interpreter


class TestDictToELBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toELBConfig_basic(self):
        output = self._run('print({"name": "web-lb"}.toELBConfig())')
        assert output[-1] == "name = web-lb"

    def test_toELBConfig_multi(self):
        output = self._run('print({"name": "web-lb", "scheme": "internet-facing"}.toELBConfig())')
        assert "name = web-lb" in output[-1]
