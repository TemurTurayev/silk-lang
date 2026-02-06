"""
Tests for array .at() and string .at() safe access methods.
"""

from silk.interpreter import Interpreter


class TestArrayAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_at_valid(self):
        output = self._run('''
print([10, 20, 30].at(1))
''')
        assert output[-1] == "20"

    def test_at_negative(self):
        output = self._run('''
print([10, 20, 30].at(-1))
''')
        assert output[-1] == "30"

    def test_at_out_of_bounds(self):
        output = self._run('''
print([10, 20, 30].at(99))
''')
        assert output[-1] == "null"

    def test_at_negative_out_of_bounds(self):
        output = self._run('''
print([1, 2].at(-10))
''')
        assert output[-1] == "null"


class TestStringAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_at_valid(self):
        output = self._run('''
print("hello".at(0))
''')
        assert output[-1] == "h"

    def test_at_negative(self):
        output = self._run('''
print("hello".at(-1))
''')
        assert output[-1] == "o"

    def test_at_out_of_bounds(self):
        output = self._run('''
print("hi".at(99))
''')
        assert output[-1] == "null"
