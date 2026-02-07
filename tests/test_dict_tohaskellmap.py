"""
Tests for dict .toHaskellMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToHaskellMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHaskellMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toHaskellMap())
''')
        assert output[-1] == 'fromList [("name", "Bob")]'

    def test_toHaskellMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toHaskellMap())
''')
        assert output[-1] == 'fromList [("port", 8080)]'
