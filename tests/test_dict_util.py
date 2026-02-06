"""
Tests for dict .isEmpty() and .count() methods.
"""

from silk.interpreter import Interpreter


class TestDictIsEmpty:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEmpty_empty(self):
        output = self._run('''
print({:}.isEmpty())
''')
        assert output[-1] == "true"

    def test_isEmpty_not_empty(self):
        output = self._run('''
print({"a": 1}.isEmpty())
''')
        assert output[-1] == "false"


class TestDictCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_count_all_match(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.count(|k, v| v > 0))
''')
        assert output[-1] == "3"

    def test_count_some_match(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.count(|k, v| v > 1))
''')
        assert output[-1] == "2"

    def test_count_none_match(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
print(m.count(|k, v| v > 10))
''')
        assert output[-1] == "0"
