"""
Tests for number .pow() and .sqrt() methods.
"""

from silk.interpreter import Interpreter


class TestNumberPow:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pow_basic(self):
        output = self._run('''
print(2.pow(10))
''')
        assert output[-1] == "1024"

    def test_pow_zero(self):
        output = self._run('''
print(5.pow(0))
''')
        assert output[-1] == "1"

    def test_sqrt_basic(self):
        output = self._run('''
print(16.sqrt())
''')
        assert output[-1] == "4"

    def test_sqrt_float(self):
        output = self._run('''
print(2.sqrt().toFixed(4))
''')
        assert output[-1] == "1.4142"

    def test_sign_positive(self):
        output = self._run('''
print(42.sign())
''')
        assert output[-1] == "1"

    def test_sign_negative(self):
        output = self._run('''
print((-5).sign())
''')
        assert output[-1] == "-1"

    def test_sign_zero(self):
        output = self._run('''
print(0.sign())
''')
        assert output[-1] == "0"
