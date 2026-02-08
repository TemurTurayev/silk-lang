"""
Tests for dict .toCockroachDBConfig() method - CockroachDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToCockroachDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCockroachDBConfig_basic(self):
        output = self._run('''
let d = {"store": "/data"}
print(d.toCockroachDBConfig())
''')
        assert output[-1] == "store=/data"

    def test_toCockroachDBConfig_number(self):
        output = self._run('''
let d = {"port": 26257}
print(d.toCockroachDBConfig())
''')
        assert output[-1] == "port=26257"
