"""
Tests for array .mapBitAlign1180591620717411303424() method - align up to nearest multiple of 1180591620717411303424.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1180591620717411303424:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1180591620717411303424_basic(self):
        output = self._run('print([0, 1, 590295810358705651711, 590295810358705651712, 1180591620717411303424].mapBitAlign1180591620717411303424())')
        assert output[-1] == '[0, 1180591620717411303424, 1180591620717411303424, 1180591620717411303424, 1180591620717411303424]'

    def test_mapBitAlign1180591620717411303424_exact(self):
        output = self._run('print([2361183241434822606848, 3541774862152233910272].mapBitAlign1180591620717411303424())')
        assert output[-1] == '[2361183241434822606848, 3541774862152233910272]'
