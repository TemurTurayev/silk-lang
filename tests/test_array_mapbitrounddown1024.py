"""
Tests for array .mapBitRoundDown1024() method - round down to nearest multiple of 1024.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown1024:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown1024_basic(self):
        output = self._run('print([1023, 1024, 1025, 2047].mapBitRoundDown1024())')
        # 1023->0, 1024->1024, 1025->1024, 2047->1024
        assert output[-1] == '[0, 1024, 1024, 1024]'

    def test_mapBitRoundDown1024_exact(self):
        output = self._run('print([0, 2048, 3072, 4096].mapBitRoundDown1024())')
        assert output[-1] == '[0, 2048, 3072, 4096]'
