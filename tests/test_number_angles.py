"""
Tests for number .toRadians() and .toDegrees() methods.
"""

from silk.interpreter import Interpreter


class TestNumberAngles:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRadians_90(self):
        output = self._run('''
print(90.toRadians().toFixed(4))
''')
        assert output[-1] == "1.5708"

    def test_toRadians_180(self):
        output = self._run('''
print(180.toRadians().toFixed(4))
''')
        assert output[-1] == "3.1416"

    def test_toDegrees_pi(self):
        output = self._run('''
print(3.14159265.toDegrees().toFixed(1))
''')
        assert output[-1] == "180.0"

    def test_toRadians_zero(self):
        output = self._run('''
print(0.toRadians())
''')
        assert output[-1] == "0"
