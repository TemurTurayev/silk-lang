"""
Tests for array .min(), .max(), and .sum() methods.
"""

from silk.interpreter import Interpreter


class TestArrayMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_min_ints(self):
        output = self._run('''
print([3, 1, 2].min())
''')
        assert output[-1] == "1"

    def test_min_negative(self):
        output = self._run('''
print([5, -3, 0, 2].min())
''')
        assert output[-1] == "-3"

    def test_min_single(self):
        output = self._run('''
print([42].min())
''')
        assert output[-1] == "42"


class TestArrayMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_max_ints(self):
        output = self._run('''
print([3, 1, 2].max())
''')
        assert output[-1] == "3"

    def test_max_negative(self):
        output = self._run('''
print([-5, -3, -1].max())
''')
        assert output[-1] == "-1"

    def test_max_single(self):
        output = self._run('''
print([42].max())
''')
        assert output[-1] == "42"


class TestArraySum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sum_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].sum())
''')
        assert output[-1] == "15"

    def test_sum_empty(self):
        output = self._run('''
print([].sum())
''')
        assert output[-1] == "0"

    def test_sum_single(self):
        output = self._run('''
print([42].sum())
''')
        assert output[-1] == "42"

    def test_sum_negative(self):
        output = self._run('''
print([1, -1, 2, -2].sum())
''')
        assert output[-1] == "0"
