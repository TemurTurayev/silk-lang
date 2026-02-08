"""
Tests for dict .toMemcachedConfig() method - Memcached config format.
"""

from silk.interpreter import Interpreter


class TestDictToMemcachedConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMemcachedConfig_basic(self):
        output = self._run('''
let d = {"port": 11211}
print(d.toMemcachedConfig())
''')
        assert output[-1] == '-port 11211'

    def test_toMemcachedConfig_string(self):
        output = self._run('''
let d = {"listen": "127.0.0.1"}
print(d.toMemcachedConfig())
''')
        assert output[-1] == '-listen 127.0.0.1'
