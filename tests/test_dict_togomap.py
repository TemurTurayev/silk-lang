"""
Tests for dict .toGoMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToGoMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGoMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toGoMap())
''')
        assert output[-1] == 'map[string]interface{}{"name": "Bob"}'

    def test_toGoMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toGoMap())
''')
        assert output[-1] == 'map[string]interface{}{"port": 8080}'
