"""
Tests for number .percent() and .percentOf() methods.
"""

from silk.interpreter import Interpreter


class TestNumberPercent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_percent_basic(self):
        output = self._run('''
print(50.percent())
''')
        assert output[-1] == "0.5"

    def test_percent_hundred(self):
        output = self._run('''
print(100.percent())
''')
        assert output[-1] == "1"

    def test_percentOf(self):
        output = self._run('''
print(25.percentOf(200))
''')
        assert output[-1] == "50"

    def test_percentOf_float(self):
        output = self._run('''
print(10.percentOf(50))
''')
        assert output[-1] == "5"
