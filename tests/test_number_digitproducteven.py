"""
Tests for number .digitProductEven() method - product of even digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitProductEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitProductEven_basic(self):
        output = self._run('print(2468.digitProductEven())')
        # 2 * 4 * 6 * 8 = 384
        assert output[-1] == "384"

    def test_digitProductEven_mixed(self):
        output = self._run('print(1234.digitProductEven())')
        # even digits: 2, 4 -> 2 * 4 = 8
        assert output[-1] == "8"
