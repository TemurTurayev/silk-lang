"""
Tests for number .motzkin() method - Motzkin number.
"""

from silk.interpreter import Interpreter


class TestNumberMotzkin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_motzkin_0(self):
        output = self._run('print(0.motzkin())')
        assert output[-1] == "1"

    def test_motzkin_3(self):
        output = self._run('print(3.motzkin())')
        assert output[-1] == "4"

    def test_motzkin_5(self):
        output = self._run('print(5.motzkin())')
        assert output[-1] == "21"
