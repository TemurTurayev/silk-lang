"""
Tests for dict .reject(fn) method.
"""

from silk.interpreter import Interpreter


class TestDictReject:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reject_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.reject(|k, v| v > 1))
''')
        assert output[-1] == '{"a": 1}'

    def test_reject_none(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
print(d.reject(|k, v| v > 100))
''')
        assert output[-1] == '{"x": 10, "y": 20}'
