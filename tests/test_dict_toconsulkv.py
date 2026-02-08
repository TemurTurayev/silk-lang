"""
Tests for dict .toConsulKV() method - convert dict to Consul KV format.
"""

from silk.interpreter import Interpreter


class TestDictToConsulKV:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConsulKV_basic(self):
        output = self._run('''
let d = {"service/name": "api"}
print(d.toConsulKV())
''')
        assert output[-1] == 'service/name: api'

    def test_toConsulKV_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toConsulKV())
''')
        assert output[-1] == 'port: 8080'
