"""
Tests for dict .defaults() method.
"""

from silk.interpreter import Interpreter


class TestDictDefaults:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_defaults_fills_missing(self):
        output = self._run('''
let config = {"host": "localhost"}
let withDefaults = config.defaults({"host": "0.0.0.0", "port": 8080})
print(withDefaults.get("host"))
print(withDefaults.get("port"))
''')
        assert output[-2] == "localhost"
        assert output[-1] == "8080"

    def test_defaults_no_overlap(self):
        output = self._run('''
let a = {"x": 1}
let b = a.defaults({"y": 2})
print(b.length)
''')
        assert output[-1] == "2"

    def test_defaults_empty_base(self):
        output = self._run('''
let empty = {:}
let result = empty.defaults({"a": 1, "b": 2})
print(result.length)
''')
        assert output[-1] == "2"
