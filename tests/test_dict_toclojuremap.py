"""
Tests for dict .toClojureMap() method.
"""

from silk.interpreter import Interpreter


class TestDictToClojureMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toClojureMap_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toClojureMap())
''')
        assert output[-1] == '{:name "Bob"}'

    def test_toClojureMap_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toClojureMap())
''')
        assert output[-1] == "{:port 8080}"
