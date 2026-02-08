"""
Tests for dict .toSentinelConfig() method - Redis Sentinel format.
"""

from silk.interpreter import Interpreter


class TestDictToSentinelConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSentinelConfig_basic(self):
        output = self._run('''
let d = {"monitor": "mymaster"}
print(d.toSentinelConfig())
''')
        assert output[-1] == 'sentinel monitor mymaster'

    def test_toSentinelConfig_number(self):
        output = self._run('''
let d = {"down-after-milliseconds": 5000}
print(d.toSentinelConfig())
''')
        assert output[-1] == 'sentinel down-after-milliseconds 5000'
