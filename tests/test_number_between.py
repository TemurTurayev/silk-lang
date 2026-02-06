"""
Tests for number .isBetween(low, high) method.
"""

from silk.interpreter import Interpreter


class TestNumberBetween:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_between_true(self):
        output = self._run('''
print(5.isBetween(1, 10))
''')
        assert output[-1] == "true"

    def test_between_false_low(self):
        output = self._run('''
print(0.isBetween(1, 10))
''')
        assert output[-1] == "false"

    def test_between_false_high(self):
        output = self._run('''
print(11.isBetween(1, 10))
''')
        assert output[-1] == "false"

    def test_between_inclusive_low(self):
        output = self._run('''
print(1.isBetween(1, 10))
''')
        assert output[-1] == "true"

    def test_between_inclusive_high(self):
        output = self._run('''
print(10.isBetween(1, 10))
''')
        assert output[-1] == "true"

    def test_between_float(self):
        output = self._run('''
print(3.14.isBetween(3, 4))
''')
        assert output[-1] == "true"
