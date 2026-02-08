"""
Tests for dict .toCassandraConfig() method - Cassandra config format.
"""

from silk.interpreter import Interpreter


class TestDictToCassandraConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCassandraConfig_basic(self):
        output = self._run('''
let d = {"native_transport_port": 9042}
print(d.toCassandraConfig())
''')
        assert output[-1] == 'native_transport_port: 9042'

    def test_toCassandraConfig_string(self):
        output = self._run('''
let d = {"cluster_name": "Test"}
print(d.toCassandraConfig())
''')
        assert output[-1] == 'cluster_name: Test'
