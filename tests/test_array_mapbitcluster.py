"""
Tests for array .mapBitCluster() method - count groups of consecutive set bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCluster:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCluster_basic(self):
        output = self._run('print([5, 7, 27].mapBitCluster())')
        # 5=101 -> 2 clusters, 7=111 -> 1 cluster, 27=11011 -> 2 clusters
        assert output[-1] == '[2, 1, 2]'

    def test_mapBitCluster_single(self):
        output = self._run('print([0, 1, 3, 15].mapBitCluster())')
        # 0 -> 0, 1=1 -> 1, 3=11 -> 1, 15=1111 -> 1
        assert output[-1] == '[0, 1, 1, 1]'
