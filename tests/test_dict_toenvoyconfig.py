"""
Tests for dict .toEnvoyConfig() method - Envoy proxy config format.
"""

from silk.interpreter import Interpreter


class TestDictToEnvoyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEnvoyConfig_basic(self):
        output = self._run('''
let d = {"cluster": "service_a"}
print(d.toEnvoyConfig())
''')
        assert output[-1] == 'cluster: "service_a"'

    def test_toEnvoyConfig_number(self):
        output = self._run('''
let d = {"timeout": 30}
print(d.toEnvoyConfig())
''')
        assert output[-1] == 'timeout: 30'
