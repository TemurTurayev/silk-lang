"""
Tests for dict .toScyllaDBConfig() method - ScyllaDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToScyllaDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toScyllaDBConfig_basic(self):
        output = self._run('''
let d = {"cluster_name": "test"}
print(d.toScyllaDBConfig())
''')
        assert output[-1] == 'cluster_name: test'

    def test_toScyllaDBConfig_number(self):
        output = self._run('''
let d = {"num_tokens": 256}
print(d.toScyllaDBConfig())
''')
        assert output[-1] == 'num_tokens: 256'
