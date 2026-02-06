"""
Tests for dict .swapKeyValue() method.
"""

from silk.interpreter import Interpreter


class TestDictSwapKeyValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_swapKeyValue_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.swapKeyValue())
''')
        assert output[-1] == '{1: a, 2: b, 3: c}'

    def test_swapKeyValue_strings(self):
        output = self._run('''
let d = {"hello": "world"}
print(d.swapKeyValue())
''')
        assert output[-1] == '{"world": hello}'
