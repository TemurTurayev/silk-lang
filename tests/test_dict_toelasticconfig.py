"""
Tests for dict .toElasticConfig() method - Elasticsearch config format.
"""

from silk.interpreter import Interpreter


class TestDictToElasticConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElasticConfig_basic(self):
        output = self._run('''
let d = {"cluster.name": "my-cluster"}
print(d.toElasticConfig())
''')
        assert output[-1] == 'cluster.name: my-cluster'

    def test_toElasticConfig_number(self):
        output = self._run('''
let d = {"http.port": 9200}
print(d.toElasticConfig())
''')
        assert output[-1] == 'http.port: 9200'
