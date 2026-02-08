"""
Tests for dict .toFoundationDBConfig() method - FoundationDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToFoundationDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFoundationDBConfig_basic(self):
        output = self._run('''
let d = {"cluster_file": "/etc/foundationdb/fdb.cluster"}
print(d.toFoundationDBConfig())
''')
        assert output[-1] == 'cluster_file = /etc/foundationdb/fdb.cluster'

    def test_toFoundationDBConfig_number(self):
        output = self._run('''
let d = {"memory": 8}
print(d.toFoundationDBConfig())
''')
        assert output[-1] == 'memory = 8'
