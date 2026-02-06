"""
Tests for number .toString() method.
"""

from silk.interpreter import Interpreter


class TestNumberToString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_int_toString(self):
        output = self._run('''
let x = 42
let s = x.toString()
print(typeof s)
print(s)
''')
        assert output[-2] == "string"
        assert output[-1] == "42"

    def test_float_toString(self):
        output = self._run('''
let x = 3.14
let s = x.toString()
print(typeof s)
print(s)
''')
        assert output[-2] == "string"
        assert output[-1] == "3.14"

    def test_negative_toString(self):
        output = self._run('''
print((-5).toString())
''')
        assert output[-1] == "-5"

    def test_toString_concat(self):
        output = self._run('''
let n = 42
print("value: " + n.toString())
''')
        assert output[-1] == "value: 42"
