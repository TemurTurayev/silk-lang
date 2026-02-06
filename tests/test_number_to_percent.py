"""
Tests for number .toPercent() method.
"""

from silk.interpreter import Interpreter


class TestNumberToPercent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPercent_basic(self):
        output = self._run('''
print(0.5.toPercent())
''')
        assert output[-1] == "50%"

    def test_toPercent_whole(self):
        output = self._run('''
print(1.toPercent())
''')
        assert output[-1] == "100%"

    def test_toPercent_zero(self):
        output = self._run('''
print(0.toPercent())
''')
        assert output[-1] == "0%"

    def test_toPercent_fraction(self):
        output = self._run('''
print(0.333.toPercent())
''')
        assert output[-1] == "33.3%"
