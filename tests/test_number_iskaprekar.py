"""
Tests for number .isKaprekar() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsKaprekar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isKaprekar_true_45(self):
        output = self._run('print(45.isKaprekar())')
        assert output[-1] == "true"

    def test_isKaprekar_true_9(self):
        output = self._run('print(9.isKaprekar())')
        assert output[-1] == "true"

    def test_isKaprekar_false(self):
        output = self._run('print(11.isKaprekar())')
        assert output[-1] == "false"
