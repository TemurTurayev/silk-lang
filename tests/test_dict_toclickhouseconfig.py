"""
Tests for dict .toClickHouseConfig() method - ClickHouse config format.
"""

from silk.interpreter import Interpreter


class TestDictToClickHouseConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toClickHouseConfig_basic(self):
        output = self._run('''
let d = {"http_port": 8123}
print(d.toClickHouseConfig())
''')
        assert output[-1] == 'http_port = 8123'

    def test_toClickHouseConfig_string(self):
        output = self._run('''
let d = {"listen_host": "0.0.0.0"}
print(d.toClickHouseConfig())
''')
        assert output[-1] == 'listen_host = 0.0.0.0'
