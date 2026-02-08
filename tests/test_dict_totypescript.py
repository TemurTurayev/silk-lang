"""
Tests for dict .toTypeScript() method - convert dict to TypeScript interface.
"""

from silk.interpreter import Interpreter


class TestDictToTypeScript:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTypeScript_string(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toTypeScript())
''')
        assert output[-1] == 'interface Data { name: string; }'

    def test_toTypeScript_number(self):
        output = self._run('''
let d = {"age": 30}
print(d.toTypeScript())
''')
        assert output[-1] == 'interface Data { age: number; }'
