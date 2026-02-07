"""
Tests for number .subfactorial() method - alias for derangements.
"""

from silk.interpreter import Interpreter


class TestNumberSubfactorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_subfactorial_3(self):
        output = self._run('print(3.subfactorial())')
        assert output[-1] == "2"

    def test_subfactorial_5(self):
        output = self._run('print(5.subfactorial())')
        assert output[-1] == "44"
