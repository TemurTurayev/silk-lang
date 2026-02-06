"""
Tests for number methods (.abs(), .floor(), .ceil(), .round()).
"""

from silk.interpreter import Interpreter


class TestNumberAbs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_abs_negative(self):
        output = self._run('''
let x = -5
print(x.abs())
''')
        assert output[-1] == "5"

    def test_abs_positive(self):
        output = self._run('''
let x = 5
print(x.abs())
''')
        assert output[-1] == "5"

    def test_abs_zero(self):
        output = self._run('''
let x = 0
print(x.abs())
''')
        assert output[-1] == "0"

    def test_abs_float(self):
        output = self._run('''
let x = -3.14
print(x.abs())
''')
        assert output[-1] == "3.14"


class TestNumberFloor:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_floor_basic(self):
        output = self._run('''
let x = 3.7
print(x.floor())
''')
        assert output[-1] == "3"

    def test_floor_negative(self):
        output = self._run('''
let x = -2.3
print(x.floor())
''')
        assert output[-1] == "-3"

    def test_floor_integer(self):
        output = self._run('''
let x = 5
print(x.floor())
''')
        assert output[-1] == "5"


class TestNumberCeil:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_ceil_basic(self):
        output = self._run('''
let x = 3.2
print(x.ceil())
''')
        assert output[-1] == "4"

    def test_ceil_negative(self):
        output = self._run('''
let x = -2.7
print(x.ceil())
''')
        assert output[-1] == "-2"


class TestNumberRound:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_round_up(self):
        output = self._run('''
let x = 3.7
print(x.round())
''')
        assert output[-1] == "4"

    def test_round_down(self):
        output = self._run('''
let x = 3.2
print(x.round())
''')
        assert output[-1] == "3"
