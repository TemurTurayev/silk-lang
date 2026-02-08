"""
Tests for dict .toNginxConfig() method - convert dict to nginx-style config.
"""

from silk.interpreter import Interpreter


class TestDictToNginxConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNginxConfig_basic(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toNginxConfig())
''')
        assert output[-1] == 'port 8080;'

    def test_toNginxConfig_string(self):
        output = self._run('''
let d = {"root": "/var/www"}
print(d.toNginxConfig())
''')
        assert output[-1] == 'root "/var/www";'
