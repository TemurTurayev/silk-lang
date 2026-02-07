"""
Tests for dict .toDotNotation() method - flatten nested dict.
"""

from silk.interpreter import Interpreter


class TestDictToDotNotation:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDotNotation_nested(self):
        output = self._run('''
let d = {"a": {"b": 1, "c": 2}}
let flat = d.toDotNotation()
print(flat.get("a.b"))
''')
        assert output[-1] == "1"

    def test_toDotNotation_shallow(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
let flat = d.toDotNotation()
print(flat.get("x"))
''')
        assert output[-1] == "1"
