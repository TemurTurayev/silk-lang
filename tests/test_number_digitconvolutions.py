"""
Tests for number .digitConvolutions() method - convolution of digit sequence with itself (first 2 elements).
"""

from silk.interpreter import Interpreter


class TestNumberDigitConvolutions:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitConvolutions_basic(self):
        output = self._run('print(123.digitConvolutions())')
        # dot product pairs: d[0]*d[0], d[0]*d[1]+d[1]*d[0], ... simplified: sum of squares, then cross
        # Actually: conv[k] = sum(d[i]*d[k-i]) for valid i
        # k=0: 1*1 = 1, k=1: 1*2+2*1 = 4, k=2: 1*3+2*2+3*1 = 10, k=3: 2*3+3*2 = 12, k=4: 3*3 = 9
        assert output[-1] == "[1, 4, 10, 12, 9]"

    def test_digitConvolutions_two(self):
        output = self._run('print(12.digitConvolutions())')
        # k=0: 1*1=1, k=1: 1*2+2*1=4, k=2: 2*2=4
        assert output[-1] == "[1, 4, 4]"
