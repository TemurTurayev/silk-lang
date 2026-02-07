"""
Tests for dict .toScalaMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToScalaMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toScalaMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toScalaMap())
''')
        assert output[-1] == 'Map("name" -> "Bob")'

    def test_toScalaMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toScalaMap())
''')
        assert output[-1] == 'Map("port" -> 8080)'
