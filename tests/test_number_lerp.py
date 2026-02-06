"""
Tests for number .lerp() method (linear interpolation).
"""

from silk.interpreter import Interpreter


class TestNumberLerp:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lerp_midpoint(self):
        output = self._run('''
print(0.lerp(10, 0.5))
''')
        assert output[-1] == "5"

    def test_lerp_start(self):
        output = self._run('''
print(0.lerp(100, 0))
''')
        assert output[-1] == "0"

    def test_lerp_end(self):
        output = self._run('''
print(0.lerp(100, 1))
''')
        assert output[-1] == "100"

    def test_lerp_quarter(self):
        output = self._run('''
print(10.lerp(20, 0.25))
''')
        assert output[-1] == "12.5"
