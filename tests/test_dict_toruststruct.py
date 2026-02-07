"""
Tests for dict .toRustStruct() method.
"""

from silk.interpreter import Interpreter


class TestDictToRustStruct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRustStruct_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toRustStruct())
''')
        assert output[-1] == 'Data { name: "Bob" }'

    def test_toRustStruct_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toRustStruct())
''')
        assert output[-1] == "Data { port: 8080 }"
