"""
Tests for dict .count(predicate) method.
"""

from silk.interpreter import Interpreter


class TestDictCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_count_values(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3}
print(d.count(|k, v| v > 2))
''')
        assert output[-1] == "2"

    def test_count_all(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
print(d.count(|k, v| v > 0))
''')
        assert output[-1] == "2"

    def test_count_none(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.count(|k, v| v > 10))
''')
        assert output[-1] == "0"
