"""
Tests for number .digitFrequency() method - count of each digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitFrequency:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitFrequency_112233(self):
        output = self._run('print(112233.digitFrequency())')
        assert output[-1] == '{1: 2, 2: 2, 3: 2}'

    def test_digitFrequency_1000(self):
        output = self._run('print(1000.digitFrequency())')
        assert output[-1] == '{1: 1, 0: 3}'
