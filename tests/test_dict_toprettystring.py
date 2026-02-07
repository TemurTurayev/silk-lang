"""
Tests for dict .toPrettyString() method.
"""

from silk.interpreter import Interpreter


class TestDictToPrettyString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPrettyString_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.toPrettyString())
''')
        assert "a" in output[-1]
        assert "1" in output[-1]

    def test_toPrettyString_format(self):
        output = self._run('''
let d = {"x": 10}
print(d.toPrettyString())
''')
        assert output[-1] == '{\n  x: 10\n}'
