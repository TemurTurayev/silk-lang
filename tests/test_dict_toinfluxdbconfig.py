"""
Tests for dict .toInfluxDBConfig() method - InfluxDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToInfluxDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInfluxDBConfig_basic(self):
        output = self._run('''
let d = {"port": 8086}
print(d.toInfluxDBConfig())
''')
        assert output[-1] == 'port = 8086'

    def test_toInfluxDBConfig_string(self):
        output = self._run('''
let d = {"bind-address": "localhost"}
print(d.toInfluxDBConfig())
''')
        assert output[-1] == 'bind-address = localhost'
