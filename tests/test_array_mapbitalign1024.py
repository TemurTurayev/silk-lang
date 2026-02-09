"""
Tests for array .mapBitAlign1024() method - align up to nearest multiple of 1024.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1024:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1024_basic(self):
        output = self._run('print([1, 1023, 1024, 1025, 2047, 2048].mapBitAlign1024())')
        # 1->1024, 1023->1024, 1024->1024, 1025->2048, 2047->2048, 2048->2048
        assert output[-1] == '[1024, 1024, 1024, 2048, 2048, 2048]'

    def test_mapBitAlign1024_zero(self):
        output = self._run('print([0, 3072, 4096].mapBitAlign1024())')
        assert output[-1] == '[0, 3072, 4096]'
