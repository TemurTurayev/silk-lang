"""
Tests for dict .toGrafanaConfig() method - Grafana-style config.
"""

from silk.interpreter import Interpreter


class TestDictToGrafanaConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGrafanaConfig_basic(self):
        output = self._run('''
let d = {"server": "localhost"}
print(d.toGrafanaConfig())
''')
        assert output[-1] == 'server = localhost'

    def test_toGrafanaConfig_number(self):
        output = self._run('''
let d = {"port": 3000}
print(d.toGrafanaConfig())
''')
        assert output[-1] == 'port = 3000'
