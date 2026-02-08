"""
Tests for string .toRailFence(rails) method - Rail fence cipher.
"""

from silk.interpreter import Interpreter


class TestStringToRailFence:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRailFence_3rails(self):
        output = self._run('print("WEAREDISCOVERED".toRailFence(3))')
        assert output[-1] == "WECRERDSOEEAIVD"

    def test_toRailFence_2rails(self):
        output = self._run('print("HELLO".toRailFence(2))')
        assert output[-1] == "HLOEL"
