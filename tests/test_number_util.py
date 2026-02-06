"""
Tests for number .isEven(), .isOdd(), .clamp() methods.
"""

from silk.interpreter import Interpreter


class TestNumberIsEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEven_true(self):
        output = self._run('''
print((4).isEven())
''')
        assert output[-1] == "true"

    def test_isEven_false(self):
        output = self._run('''
print((3).isEven())
''')
        assert output[-1] == "false"

    def test_isEven_zero(self):
        output = self._run('''
print((0).isEven())
''')
        assert output[-1] == "true"


class TestNumberIsOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isOdd_true(self):
        output = self._run('''
print((3).isOdd())
''')
        assert output[-1] == "true"

    def test_isOdd_false(self):
        output = self._run('''
print((4).isOdd())
''')
        assert output[-1] == "false"


class TestNumberClamp:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_clamp_within_range(self):
        output = self._run('''
let x = 5
print(x.clamp(0, 10))
''')
        assert output[-1] == "5"

    def test_clamp_below_min(self):
        output = self._run('''
let x = -5
print(x.clamp(0, 10))
''')
        assert output[-1] == "0"

    def test_clamp_above_max(self):
        output = self._run('''
let x = 15
print(x.clamp(0, 10))
''')
        assert output[-1] == "10"

    def test_clamp_at_boundary(self):
        output = self._run('''
print((0).clamp(0, 10))
print((10).clamp(0, 10))
''')
        assert output[-2] == "0"
        assert output[-1] == "10"
