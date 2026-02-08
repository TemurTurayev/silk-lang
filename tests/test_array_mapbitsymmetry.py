"""
Tests for array .mapBitSymmetry() method - check if binary representation is a palindrome.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSymmetry:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSymmetry_basic(self):
        output = self._run('print([5, 3, 9].mapBitSymmetry())')
        # 5=101 palindrome=true, 3=11 palindrome=true, 9=1001 palindrome=true
        assert output[-1] == '[true, true, true]'

    def test_mapBitSymmetry_false(self):
        output = self._run('print([2, 6, 10].mapBitSymmetry())')
        # 2=10 no, 6=110 no, 10=1010 no
        assert output[-1] == '[false, false, false]'
