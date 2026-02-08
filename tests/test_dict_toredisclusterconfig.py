"""
Tests for dict .toRedisClusterConfig() method - Redis cluster config format.
"""

from silk.interpreter import Interpreter


class TestDictToRedisClusterConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedisClusterConfig_basic(self):
        output = self._run('''
let d = {"port": 6379}
print(d.toRedisClusterConfig())
''')
        assert output[-1] == 'cluster-port 6379'

    def test_toRedisClusterConfig_string(self):
        output = self._run('''
let d = {"announce-ip": "10.0.0.1"}
print(d.toRedisClusterConfig())
''')
        assert output[-1] == 'cluster-announce-ip 10.0.0.1'
