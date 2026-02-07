"""
Tests for dict .fromDotNotation() method - expand dot keys to nested dict.
"""

from silk.interpreter import Interpreter


class TestDictFromDotNotation:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fromDotNotation_nested(self):
        output = self._run('''
let d = {"a.b": 1, "a.c": 2}
let nested = d.fromDotNotation()
print(nested.get("a").get("b"))
''')
        assert output[-1] == "1"

    def test_fromDotNotation_shallow(self):
        output = self._run('''
let d = {"x": 1}
let nested = d.fromDotNotation()
print(nested.get("x"))
''')
        assert output[-1] == "1"
