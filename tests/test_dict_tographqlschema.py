"""
Tests for dict .toGraphQLSchema() method - convert dict to GraphQL schema type.
"""

from silk.interpreter import Interpreter


class TestDictToGraphQLSchema:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGraphQLSchema_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
print(d.toGraphQLSchema())
''')
        assert "type Data {" in output[-1]
        assert "name: String" in output[-1]
        assert "age: Int" in output[-1]

    def test_toGraphQLSchema_bool(self):
        output = self._run('''
let d = {"active": true}
print(d.toGraphQLSchema())
''')
        assert "active: Boolean" in output[-1]
