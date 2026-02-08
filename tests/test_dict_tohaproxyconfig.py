"""
Tests for dict .toHAProxyConfig() method - HAProxy format.
"""

from silk.interpreter import Interpreter


class TestDictToHAProxyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHAProxyConfig_basic(self):
        output = self._run('''
let d = {"mode": "http"}
print(d.toHAProxyConfig())
''')
        assert output[-1] == 'mode http'

    def test_toHAProxyConfig_number(self):
        output = self._run('''
let d = {"maxconn": 4096}
print(d.toHAProxyConfig())
''')
        assert output[-1] == 'maxconn 4096'
