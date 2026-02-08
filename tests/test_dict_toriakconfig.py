"""
Tests for dict .toRiakConfig() method - Riak config format.
"""

from silk.interpreter import Interpreter


class TestDictToRiakConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRiakConfig_basic(self):
        output = self._run('''
let d = {"nodename": "riak@127.0.0.1"}
print(d.toRiakConfig())
''')
        assert output[-1] == 'nodename = riak@127.0.0.1'

    def test_toRiakConfig_number(self):
        output = self._run('''
let d = {"ring_size": 64}
print(d.toRiakConfig())
''')
        assert output[-1] == 'ring_size = 64'
