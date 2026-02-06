"""
Tests for number .toFixed() decimal formatting.
"""

from silk.interpreter import Interpreter


class TestNumberFormat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFixed_two_decimals(self):
        output = self._run('''
print(3.14159.toFixed(2))
''')
        assert output[-1] == "3.14"

    def test_toFixed_zero_decimals(self):
        output = self._run('''
print(3.7.toFixed(0))
''')
        assert output[-1] == "4"

    def test_toFixed_int(self):
        output = self._run('''
print(42.toFixed(2))
''')
        assert output[-1] == "42.00"

    def test_toFixed_one_decimal(self):
        output = self._run('''
print(2.5.toFixed(1))
''')
        assert output[-1] == "2.5"
