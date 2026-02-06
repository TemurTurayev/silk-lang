"""
Tests for number .toScientific() method.
"""

from silk.interpreter import Interpreter


class TestNumberToScientific:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toScientific_large(self):
        output = self._run('print(1500.toScientific())')
        assert output[-1] == "1.5e+03"

    def test_toScientific_small(self):
        output = self._run('print(42.toScientific())')
        assert output[-1] == "4.2e+01"

    def test_toScientific_zero(self):
        output = self._run('print(0.toScientific())')
        assert output[-1] == "0.0e+00"
