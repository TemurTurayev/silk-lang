"""
Tests for dict .toPairs() method.
"""

from silk.interpreter import Interpreter


class TestDictToPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPairs_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let p = d.toPairs()
print(p.length)
''')
        assert output[-1] == "2"

    def test_toPairs_structure(self):
        output = self._run('''
let d = {"x": 10}
let p = d.toPairs()
print(p[0][0])
print(p[0][1])
''')
        assert output[0] == "x"
        assert output[1] == "10"
