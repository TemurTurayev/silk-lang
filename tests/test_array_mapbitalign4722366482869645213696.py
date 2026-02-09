"""
Tests for array .mapBitAlign4722366482869645213696() method - align up to nearest multiple of 4722366482869645213696.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4722366482869645213696:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4722366482869645213696_basic(self):
        output = self._run('print([0, 1, 2361183241434822606847, 2361183241434822606848, 4722366482869645213696].mapBitAlign4722366482869645213696())')
        assert output[-1] == '[0, 4722366482869645213696, 4722366482869645213696, 4722366482869645213696, 4722366482869645213696]'

    def test_mapBitAlign4722366482869645213696_exact(self):
        output = self._run('print([9444732965739290427392, 14167099448608935641088].mapBitAlign4722366482869645213696())')
        assert output[-1] == '[9444732965739290427392, 14167099448608935641088]'
