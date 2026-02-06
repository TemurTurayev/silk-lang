"""
Tests for number .clampMin() and .clampMax() methods.
"""

from silk.interpreter import Interpreter


class TestNumberClampMinMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_clampMin_below(self):
        output = self._run('''
print(3.clampMin(5))
''')
        assert output[-1] == "5"

    def test_clampMin_above(self):
        output = self._run('''
print(10.clampMin(5))
''')
        assert output[-1] == "10"

    def test_clampMax_above(self):
        output = self._run('''
print(10.clampMax(5))
''')
        assert output[-1] == "5"

    def test_clampMax_below(self):
        output = self._run('''
print(3.clampMax(5))
''')
        assert output[-1] == "3"
