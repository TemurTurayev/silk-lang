"""
Tests for array .mapBitAlign295147905179352825856() method - align up to nearest multiple of 295147905179352825856.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign295147905179352825856:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign295147905179352825856_basic(self):
        output = self._run('print([0, 1, 147573952589676412927, 147573952589676412928, 295147905179352825856].mapBitAlign295147905179352825856())')
        assert output[-1] == '[0, 295147905179352825856, 295147905179352825856, 295147905179352825856, 295147905179352825856]'

    def test_mapBitAlign295147905179352825856_exact(self):
        output = self._run('print([590295810358705651712, 885443715538058477568].mapBitAlign295147905179352825856())')
        assert output[-1] == '[590295810358705651712, 885443715538058477568]'
