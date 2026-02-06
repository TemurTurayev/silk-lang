"""
Tests for array .zip() method.
"""

from silk.interpreter import Interpreter


class TestArrayZipMethod:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zip_basic(self):
        output = self._run('''
let a = [1, 2, 3]
let b = ["a", "b", "c"]
let zipped = a.zip(b)
print(zipped[0])
print(zipped[1])
print(zipped[2])
''')
        assert output[0] == "[1, a]"
        assert output[1] == "[2, b]"
        assert output[2] == "[3, c]"

    def test_zip_different_lengths(self):
        output = self._run('''
let a = [1, 2, 3]
let b = ["x", "y"]
let zipped = a.zip(b)
print(zipped.length)
''')
        assert output[-1] == "2"

    def test_zip_empty(self):
        output = self._run('''
let zipped = [].zip([1, 2])
print(zipped.length)
''')
        assert output[-1] == "0"
