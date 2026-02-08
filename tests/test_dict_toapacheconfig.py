"""
Tests for dict .toApacheConfig() method - convert dict to Apache config directives.
"""

from silk.interpreter import Interpreter


class TestDictToApacheConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toApacheConfig_basic(self):
        output = self._run('''
let d = {"ServerName": "example.com"}
print(d.toApacheConfig())
''')
        assert output[-1] == 'ServerName "example.com"'

    def test_toApacheConfig_number(self):
        output = self._run('''
let d = {"Listen": 8080}
print(d.toApacheConfig())
''')
        assert output[-1] == 'Listen 8080'
