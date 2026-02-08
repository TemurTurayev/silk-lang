"""
Tests for dict .toLogstashConfig() method - Logstash format.
"""

from silk.interpreter import Interpreter


class TestDictToLogstashConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLogstashConfig_basic(self):
        output = self._run('''
let d = {"host": "localhost"}
print(d.toLogstashConfig())
''')
        assert output[-1] == 'host => "localhost"'

    def test_toLogstashConfig_number(self):
        output = self._run('''
let d = {"port": 5044}
print(d.toLogstashConfig())
''')
        assert output[-1] == 'port => 5044'
