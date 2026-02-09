"""
Tests for array .mapBitQuantize1024() method - quantize to nearest multiple of 1024.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize1024:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize1024_basic(self):
        output = self._run('print([10, 1025, 2048, 3000].mapBitQuantize1024())')
        # 10->0, 1025->1024, 2048->2048, 3000->2048
        assert output[-1] == '[0, 1024, 2048, 2048]'

    def test_mapBitQuantize1024_exact(self):
        output = self._run('print([0, 1024, 2048, 3072].mapBitQuantize1024())')
        assert output[-1] == '[0, 1024, 2048, 3072]'
