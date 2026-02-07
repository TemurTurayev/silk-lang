"""
Tests for number .isAutomorphic() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsAutomorphic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAutomorphic_true_25(self):
        output = self._run('print(25.isAutomorphic())')
        assert output[-1] == "true"

    def test_isAutomorphic_true_76(self):
        output = self._run('print(76.isAutomorphic())')
        assert output[-1] == "true"

    def test_isAutomorphic_false(self):
        output = self._run('print(13.isAutomorphic())')
        assert output[-1] == "false"
