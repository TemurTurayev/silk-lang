"""
Tests for number .isPositive(), .isNegative(), .isZero() methods.
"""

from silk.interpreter import Interpreter


class TestNumberSignCheck:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPositive_true(self):
        output = self._run('''
print(5.isPositive())
''')
        assert output[-1] == "true"

    def test_isPositive_false(self):
        output = self._run('''
print((-3).isPositive())
''')
        assert output[-1] == "false"

    def test_isNegative_true(self):
        output = self._run('''
print((-7).isNegative())
''')
        assert output[-1] == "true"

    def test_isNegative_false(self):
        output = self._run('''
print(0.isNegative())
''')
        assert output[-1] == "false"

    def test_isZero_true(self):
        output = self._run('''
print(0.isZero())
''')
        assert output[-1] == "true"

    def test_isZero_false(self):
        output = self._run('''
print(1.isZero())
''')
        assert output[-1] == "false"
