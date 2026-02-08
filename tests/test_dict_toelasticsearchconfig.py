"""
Tests for dict .toElasticsearchConfig() method - Elasticsearch config format.
"""

from silk.interpreter import Interpreter


class TestDictToElasticsearchConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElasticsearchConfig_basic(self):
        output = self._run('''
let d = {"cluster.name": "my-app"}
print(d.toElasticsearchConfig())
''')
        assert output[-1] == 'cluster.name: my-app'

    def test_toElasticsearchConfig_number(self):
        output = self._run('''
let d = {"node.max_local_storage_nodes": 3}
print(d.toElasticsearchConfig())
''')
        assert output[-1] == 'node.max_local_storage_nodes: 3'
