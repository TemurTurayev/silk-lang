"""
Tests for number .oblong() method - oblong/pronic number n*(n+1).
"""

from silk.interpreter import Interpreter


class TestNumberOblong:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_oblong_3(self):
        output = self._run('print(3.oblong())')
        assert output[-1] == "12"

    def test_oblong_5(self):
        output = self._run('print(5.oblong())')
        assert output[-1] == "30"
