"""
Tests for dict .toKeyValueStrings(sep) method.
"""

from silk.interpreter import Interpreter


class TestDictToKeyValueStrings:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKeyValueStrings_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.toKeyValueStrings("="))
''')
        assert output[-1] == '[a=1, b=2]'

    def test_toKeyValueStrings_colon(self):
        output = self._run('''
let d = {"x": 10}
print(d.toKeyValueStrings(": "))
''')
        assert output[-1] == '[x: 10]'
