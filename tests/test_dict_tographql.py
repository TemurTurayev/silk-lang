"""
Tests for dict .toGraphQL() method.
"""

from silk.interpreter import Interpreter


class TestDictToGraphQL:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGraphQL_basic(self):
        output = self._run('''
let d = {"name": "Bob", "age": 30}
let gql = d.toGraphQL()
print(gql.contains("name"))
''')
        assert output[-1] == "true"

    def test_toGraphQL_braces(self):
        output = self._run('''
let d = {"x": 1}
let gql = d.toGraphQL()
print(gql.contains("{"))
''')
        assert output[-1] == "true"
