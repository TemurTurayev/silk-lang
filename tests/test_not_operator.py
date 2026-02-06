"""
Tests for ! as logical NOT (alias for not).
"""

from silk.interpreter import Interpreter


class TestNotOperator:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_bang_true(self):
        output = self._run('''
print(!true)
''')
        assert output[-1] == "false"

    def test_bang_false(self):
        output = self._run('''
print(!false)
''')
        assert output[-1] == "true"

    def test_bang_expression(self):
        output = self._run('''
let x = 5
print(!(x > 10))
''')
        assert output[-1] == "true"

    def test_bang_null(self):
        output = self._run('''
let x = null
print(!x)
''')
        assert output[-1] == "true"

    def test_bang_zero(self):
        output = self._run('''
print(!0)
''')
        assert output[-1] == "true"

    def test_double_bang(self):
        output = self._run('''
print(!!true)
''')
        assert output[-1] == "true"

    def test_bang_in_condition(self):
        output = self._run('''
let found = false
if !found {
    print("not found")
}
''')
        assert output[-1] == "not found"
