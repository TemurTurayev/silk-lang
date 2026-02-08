"""
Tests for number .digitFrequencyMap() method - map of digit to its frequency.
"""

from silk.interpreter import Interpreter


class TestNumberDigitFrequencyMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitFrequencyMap_basic(self):
        output = self._run('print(11234.digitFrequencyMap())')
        # Should produce dict-like: {1: 2, 2: 1, 3: 1, 4: 1}
        assert "1: 2" in output[-1]

    def test_digitFrequencyMap_all_same(self):
        output = self._run('print(555.digitFrequencyMap())')
        assert "5: 3" in output[-1]
