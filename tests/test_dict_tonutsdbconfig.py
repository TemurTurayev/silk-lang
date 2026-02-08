"""
Tests for dict .toNutsDBConfig() method - NutsDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToNutsDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNutsDBConfig_basic(self):
        output = self._run('''
let d = {"dir": "/data/nutsdb"}
print(d.toNutsDBConfig())
''')
        assert output[-1] == 'dir: /data/nutsdb'

    def test_toNutsDBConfig_number(self):
        output = self._run('''
let d = {"segment_size": 8388608}
print(d.toNutsDBConfig())
''')
        assert output[-1] == 'segment_size: 8388608'
