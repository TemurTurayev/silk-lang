"""
Tests for dict .minByValue() method.
"""

from silk.interpreter import Interpreter


class TestDictMinByValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_minByValue_basic(self):
        output = self._run('''
let d = {"a": 3, "b": 1, "c": 2}
print(d.minByValue())
''')
        assert output[-1] == "b"

    def test_minByValue_single(self):
        output = self._run('''
let d = {"x": 42}
print(d.minByValue())
''')
        assert output[-1] == "x"
