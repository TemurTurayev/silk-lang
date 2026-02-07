"""
Tests for dict .toEnvironment() method - export KEY=value format.
"""

from silk.interpreter import Interpreter


class TestDictToEnvironment:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEnvironment_basic(self):
        output = self._run('''
let d = {"HOST": "localhost"}
let env = d.toEnvironment()
print(env)
''')
        assert output[-1] == "export HOST=localhost"

    def test_toEnvironment_multi(self):
        output = self._run('''
let d = {"A": 1, "B": 2}
let env = d.toEnvironment()
print(env.contains("export A=1"))
''')
        assert output[-1] == "true"
