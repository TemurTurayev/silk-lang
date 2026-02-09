"""
Tests for array .mapBitAlign590295810358705651712() method - align up to nearest multiple of 590295810358705651712.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign590295810358705651712:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign590295810358705651712_basic(self):
        output = self._run('print([0, 1, 295147905179352825855, 295147905179352825856, 590295810358705651712].mapBitAlign590295810358705651712())')
        assert output[-1] == '[0, 590295810358705651712, 590295810358705651712, 590295810358705651712, 590295810358705651712]'

    def test_mapBitAlign590295810358705651712_exact(self):
        output = self._run('print([1180591620717411303424, 1770887431076116955136].mapBitAlign590295810358705651712())')
        assert output[-1] == '[1180591620717411303424, 1770887431076116955136]'
