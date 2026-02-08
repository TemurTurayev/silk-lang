"""
Tests for number .digitAdjacentParity() method - check if adjacent digits have same parity.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentParity:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentParity_mixed(self):
        output = self._run('print(1234.digitAdjacentParity())')
        # 1%2==2%2? no, 2%2==3%2? no, 3%2==4%2? no = [false, false, false]
        assert output[-1] == "[false, false, false]"

    def test_digitAdjacentParity_sameParity(self):
        output = self._run('print(2468.digitAdjacentParity())')
        # all even: [true, true, true]
        assert output[-1] == "[true, true, true]"
