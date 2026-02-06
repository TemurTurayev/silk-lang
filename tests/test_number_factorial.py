"""
Tests for number .factorial() method.
"""

from silk.interpreter import Interpreter


class TestNumberFactorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_factorial_5(self):
        output = self._run('''
print(5.factorial())
''')
        assert output[-1] == "120"

    def test_factorial_0(self):
        output = self._run('''
print(0.factorial())
''')
        assert output[-1] == "1"

    def test_factorial_1(self):
        output = self._run('''
print(1.factorial())
''')
        assert output[-1] == "1"

    def test_factorial_10(self):
        output = self._run('''
print(10.factorial())
''')
        assert output[-1] == "3628800"
