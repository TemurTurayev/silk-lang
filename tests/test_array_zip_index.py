"""
Tests for array .zipWithIndex() method.
"""

from silk.interpreter import Interpreter


class TestArrayZipWithIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zipWithIndex_basic(self):
        output = self._run('''
let result = ["a", "b", "c"].zipWithIndex()
print(result[0])
print(result[1])
print(result[2])
''')
        assert output[-3] == "[a, 0]"
        assert output[-2] == "[b, 1]"
        assert output[-1] == "[c, 2]"

    def test_zipWithIndex_length(self):
        output = self._run('''
let result = [10, 20].zipWithIndex()
print(result.length)
''')
        assert output[-1] == "2"

    def test_zipWithIndex_empty(self):
        output = self._run('''
let result = [].zipWithIndex()
print(result.length)
''')
        assert output[-1] == "0"
