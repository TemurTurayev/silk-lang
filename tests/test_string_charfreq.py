"""
Tests for string .charFrequency() method.
"""

from silk.interpreter import Interpreter


class TestStringCharFrequency:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_charFrequency_basic(self):
        output = self._run('''
let f = "aabbc".charFrequency()
print(f["a"])
print(f["b"])
print(f["c"])
''')
        assert output[0] == "2"
        assert output[1] == "2"
        assert output[2] == "1"

    def test_charFrequency_single(self):
        output = self._run('''
let f = "hello".charFrequency()
print(f["l"])
''')
        assert output[-1] == "2"
