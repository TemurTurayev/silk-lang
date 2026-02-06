"""
Tests for const declarations.
"""

from silk.interpreter import Interpreter


class TestConst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_const_basic(self):
        output = self._run('''
const x = 42
print(x)
''')
        assert output[-1] == "42"

    def test_const_string(self):
        output = self._run('''
const name = "silk"
print(name)
''')
        assert output[-1] == "silk"

    def test_const_immutable(self):
        """const should be immutable - reassigning should error."""
        interp = Interpreter()
        result = interp.run('''
const x = 10
x = 20
''')
        assert result is False

    def test_const_with_type(self):
        output = self._run('''
const pi: float = 3.14
print(pi)
''')
        assert output[-1] == "3.14"
