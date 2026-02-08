"""
Tests for number .digitRMS() method - root mean square of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRMS:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRMS_basic(self):
        output = self._run('print(333.digitRMS())')
        assert output[-1] == "3"

    def test_digitRMS_varied(self):
        output = self._run('print(12.digitRMS())')
        # sqrt((1+4)/2) = sqrt(2.5) ≈ 1.5811388300841898
        assert output[-1].startswith("1.58")
