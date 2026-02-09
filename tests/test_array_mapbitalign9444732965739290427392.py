"""
Tests for array .mapBitAlign9444732965739290427392() method - align up to nearest multiple of 9444732965739290427392.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign9444732965739290427392:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign9444732965739290427392_basic(self):
        output = self._run('print([0, 1, 4722366482869645213695, 4722366482869645213696, 9444732965739290427392].mapBitAlign9444732965739290427392())')
        assert output[-1] == '[0, 9444732965739290427392, 9444732965739290427392, 9444732965739290427392, 9444732965739290427392]'

    def test_mapBitAlign9444732965739290427392_exact(self):
        output = self._run('print([18889465931478580854784, 28334198897217871282176].mapBitAlign9444732965739290427392())')
        assert output[-1] == '[18889465931478580854784, 28334198897217871282176]'
