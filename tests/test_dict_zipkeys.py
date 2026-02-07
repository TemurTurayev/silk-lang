"""
Tests for dict .zipKeys(keys, values) static-like via array.
"""

from silk.interpreter import Interpreter


class TestDictZipKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zipKeys_basic(self):
        output = self._run('''
let keys = ["a", "b", "c"]
let vals = [1, 2, 3]
let d = keys.toDict(vals)
print(d.get("b"))
''')
        assert output[-1] == "2"

    def test_zipKeys_size(self):
        output = self._run('''
let d = ["x", "y"].toDict([10, 20])
print(d.size)
''')
        assert output[-1] == "2"
