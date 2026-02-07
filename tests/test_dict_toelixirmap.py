"""
Tests for dict .toElixirMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToElixirMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElixirMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toElixirMap())
''')
        assert output[-1] == '%{name: "Bob"}'

    def test_toElixirMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toElixirMap())
''')
        assert output[-1] == "%{port: 8080}"
