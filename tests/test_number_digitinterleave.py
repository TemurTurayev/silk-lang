"""
Tests for number .digitInterleave() method - interleave digits from front and back.
"""

from silk.interpreter import Interpreter


class TestNumberDigitInterleave:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitInterleave_basic(self):
        output = self._run('print(1234.digitInterleave())')
        # front: 1,2  back: 4,3 -> [1,4,2,3]
        assert output[-1] == "[1, 4, 2, 3]"

    def test_digitInterleave_odd(self):
        output = self._run('print(12345.digitInterleave())')
        # front: 1,2,3  back: 5,4 -> [1,5,2,4,3]
        assert output[-1] == "[1, 5, 2, 4, 3]"
