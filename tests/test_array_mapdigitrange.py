"""
Tests for array .mapDigitRange() method - range (max-min) of digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitRange:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitRange_basic(self):
        output = self._run('print([192, 333, 507].mapDigitRange())')
        # 9-1=8, 3-3=0, 7-0=7
        assert output[-1] == "[8, 0, 7]"

    def test_mapDigitRange_single(self):
        output = self._run('print([5, 19, 111].mapDigitRange())')
        # 0, 9-1=8, 0
        assert output[-1] == "[0, 8, 0]"
