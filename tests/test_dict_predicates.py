"""
Tests for dict .every() and .some() methods.
"""

from silk.interpreter import Interpreter


class TestDictPredicates:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_every_true(self):
        output = self._run('''
let m = {"a": 2, "b": 4, "c": 6}
print(m.every(|k, v| v % 2 == 0))
''')
        assert output[-1] == "true"

    def test_every_false(self):
        output = self._run('''
let m = {"a": 2, "b": 3, "c": 6}
print(m.every(|k, v| v % 2 == 0))
''')
        assert output[-1] == "false"

    def test_some_true(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.some(|k, v| v > 2))
''')
        assert output[-1] == "true"

    def test_some_false(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
print(m.some(|k, v| v > 10))
''')
        assert output[-1] == "false"

    def test_every_empty(self):
        output = self._run('''
let m = {:}
print(m.every(|k, v| v > 0))
''')
        assert output[-1] == "true"
