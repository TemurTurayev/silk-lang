"""
Tests for dict .toRedisConfig() method - Redis config format.
"""

from silk.interpreter import Interpreter


class TestDictToRedisConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedisConfig_basic(self):
        output = self._run('''
let d = {"bind": "127.0.0.1"}
print(d.toRedisConfig())
''')
        assert output[-1] == 'bind 127.0.0.1'

    def test_toRedisConfig_number(self):
        output = self._run('''
let d = {"port": 6379}
print(d.toRedisConfig())
''')
        assert output[-1] == 'port 6379'
