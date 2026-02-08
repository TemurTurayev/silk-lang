"""
Tests for dict .toPrometheusConfig() method - Prometheus-style config.
"""

from silk.interpreter import Interpreter


class TestDictToPrometheusConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPrometheusConfig_basic(self):
        output = self._run('''
let d = {"scrape_interval": "15s"}
print(d.toPrometheusConfig())
''')
        assert output[-1] == 'scrape_interval = "15s"'

    def test_toPrometheusConfig_number(self):
        output = self._run('''
let d = {"port": 9090}
print(d.toPrometheusConfig())
''')
        assert output[-1] == 'port = 9090'
