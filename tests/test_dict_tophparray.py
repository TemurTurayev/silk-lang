"""
Tests for dict .toPhpArray() method.
"""

from silk.interpreter import Interpreter


class TestDictToPhpArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPhpArray_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toPhpArray())
''')
        assert output[-1] == '["name" => "Bob"]'

    def test_toPhpArray_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toPhpArray())
''')
        assert output[-1] == '["port" => 8080]'
