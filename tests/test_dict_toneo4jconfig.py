"""
Tests for dict .toNeo4jConfig() method - Neo4j config format.
"""

from silk.interpreter import Interpreter


class TestDictToNeo4jConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeo4jConfig_basic(self):
        output = self._run('''
let d = {"port": 7474}
print(d.toNeo4jConfig())
''')
        assert output[-1] == 'port=7474'

    def test_toNeo4jConfig_string(self):
        output = self._run('''
let d = {"dbms.default_database": "neo4j"}
print(d.toNeo4jConfig())
''')
        assert output[-1] == 'dbms.default_database=neo4j'
