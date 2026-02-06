"""
Tests for array .average() and .none() methods.
"""

from silk.interpreter import Interpreter


class TestArrayAverage:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_average_basic(self):
        output = self._run('''
print([10, 20, 30].average())
''')
        assert output[-1] == "20"

    def test_average_float(self):
        output = self._run('''
print([1, 2, 3, 4].average())
''')
        assert output[-1] == "2.5"

    def test_average_single(self):
        output = self._run('''
print([7].average())
''')
        assert output[-1] == "7"


class TestArrayNone:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_none_true(self):
        output = self._run('''
print([1, 2, 3].none(|x| x > 10))
''')
        assert output[-1] == "true"

    def test_none_false(self):
        output = self._run('''
print([1, 2, 30].none(|x| x > 10))
''')
        assert output[-1] == "false"

    def test_none_empty(self):
        output = self._run('''
print([].none(|x| x > 0))
''')
        assert output[-1] == "true"
