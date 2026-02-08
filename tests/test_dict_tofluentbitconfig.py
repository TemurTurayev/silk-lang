"""
Tests for dict .toFluentBitConfig() method - Fluent Bit config format.
"""

from silk.interpreter import Interpreter


class TestDictToFluentBitConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFluentBitConfig_basic(self):
        output = self._run('''
let d = {"Name": "tail"}
print(d.toFluentBitConfig())
''')
        assert output[-1] == 'Name tail'

    def test_toFluentBitConfig_number(self):
        output = self._run('''
let d = {"Refresh_Interval": 5}
print(d.toFluentBitConfig())
''')
        assert output[-1] == 'Refresh_Interval 5'
