"""
Tests for int() and float() global type conversion builtins.
"""

from silk.interpreter import Interpreter


class TestIntConversion:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_string_to_int(self):
        output = self._run('''
print(int("42"))
''')
        assert output[-1] == "42"

    def test_float_to_int(self):
        output = self._run('''
print(int(3.7))
''')
        assert output[-1] == "3"

    def test_bool_to_int(self):
        output = self._run('''
print(int(true))
''')
        assert output[-1] == "1"

    def test_int_to_int(self):
        output = self._run('''
print(int(42))
''')
        assert output[-1] == "42"


class TestFloatConversion:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_string_to_float(self):
        output = self._run('''
print(float("3.14"))
''')
        assert output[-1] == "3.14"

    def test_int_to_float(self):
        output = self._run('''
print(float(42) + 0.1)
''')
        assert output[-1] == "42.1"

    def test_bool_to_float(self):
        output = self._run('''
print(float(false))
''')
        assert output[-1] == "0"
