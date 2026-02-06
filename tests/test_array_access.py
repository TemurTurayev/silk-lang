"""
Tests for array .first(), .last(), .isEmpty() methods.
"""

from silk.interpreter import Interpreter


class TestArrayFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_first_basic(self):
        output = self._run('''
print([10, 20, 30].first())
''')
        assert output[-1] == "10"

    def test_first_single(self):
        output = self._run('''
print([42].first())
''')
        assert output[-1] == "42"

    def test_first_empty(self):
        output = self._run('''
print([].first())
''')
        assert output[-1] == "null"


class TestArrayLast:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_last_basic(self):
        output = self._run('''
print([10, 20, 30].last())
''')
        assert output[-1] == "30"

    def test_last_single(self):
        output = self._run('''
print([42].last())
''')
        assert output[-1] == "42"

    def test_last_empty(self):
        output = self._run('''
print([].last())
''')
        assert output[-1] == "null"


class TestArrayIsEmpty:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEmpty_empty(self):
        output = self._run('''
print([].isEmpty())
''')
        assert output[-1] == "true"

    def test_isEmpty_not_empty(self):
        output = self._run('''
print([1, 2].isEmpty())
''')
        assert output[-1] == "false"
