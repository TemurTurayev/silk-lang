"""
Tests for dict .toKotlinMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToKotlinMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKotlinMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toKotlinMap())
''')
        assert output[-1] == 'mapOf("name" to "Bob")'

    def test_toKotlinMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toKotlinMap())
''')
        assert output[-1] == 'mapOf("port" to 8080)'
