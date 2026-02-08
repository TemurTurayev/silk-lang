"""
Tests for number .digitDecMin() method - min of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecMin_basic(self):
        output = self._run('print(12345678901234567890.digitDecMin())')
        # [min(1..9,0)=0, min(1..9,0)=0]
        assert output[-1] == "[0, 0]"

    def test_digitDecMin_remainder(self):
        output = self._run('print(123456789012.digitDecMin())')
        # [min(1..9,0)=0, min(1,2)=1]
        assert output[-1] == "[0, 1]"
