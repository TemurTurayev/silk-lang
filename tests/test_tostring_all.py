"""
Tests for .toString() on various types and global str() conversions.
"""

from silk.interpreter import Interpreter


class TestToStringAll:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_bool_true_tostring(self):
        output = self._run('''
print(str(true))
''')
        assert output[-1] == "true"

    def test_bool_false_tostring(self):
        output = self._run('''
print(str(false))
''')
        assert output[-1] == "false"

    def test_null_tostring(self):
        output = self._run('''
print(str(null))
''')
        assert output[-1] == "null"

    def test_array_tostring(self):
        output = self._run('''
print(str([1, 2, 3]))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_int_tostring(self):
        output = self._run('''
print(str(42))
''')
        assert output[-1] == "42"

    def test_concat_with_str(self):
        output = self._run('''
let n = 42
let b = true
print("n=" + str(n) + " b=" + str(b))
''')
        assert output[-1] == "n=42 b=true"
