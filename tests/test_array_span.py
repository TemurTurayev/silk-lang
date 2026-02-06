"""
Tests for array .span(fn) method.
"""

from silk.interpreter import Interpreter


class TestArraySpan:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_span_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].span(|x| x < 3)
print(result[0])
print(result[1])
''')
        assert output[0] == "[1, 2]"
        assert output[1] == "[3, 4, 5]"

    def test_span_all_match(self):
        output = self._run('''
let result = [1, 2, 3].span(|x| x < 10)
print(result[0])
print(result[1])
''')
        assert output[0] == "[1, 2, 3]"
        assert output[1] == "[]"

    def test_span_none_match(self):
        output = self._run('''
let result = [5, 6, 7].span(|x| x < 3)
print(result[0])
print(result[1])
''')
        assert output[0] == "[]"
        assert output[1] == "[5, 6, 7]"
