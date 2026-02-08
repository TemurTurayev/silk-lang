"""
Tests for dict .toVarnishConfig() method - Varnish format.
"""

from silk.interpreter import Interpreter


class TestDictToVarnishConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVarnishConfig_basic(self):
        output = self._run('''
let d = {"backend": "default"}
print(d.toVarnishConfig())
''')
        assert output[-1] == 'set backend = "default";'

    def test_toVarnishConfig_number(self):
        output = self._run('''
let d = {"timeout": 300}
print(d.toVarnishConfig())
''')
        assert output[-1] == 'set timeout = 300;'
