"""
Tests for dict .toEtcdConfig() method - convert dict to etcd key-value format.
"""

from silk.interpreter import Interpreter


class TestDictToEtcdConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEtcdConfig_basic(self):
        output = self._run('''
let d = {"key": "value"}
print(d.toEtcdConfig())
''')
        assert output[-1] == '/key "value"'

    def test_toEtcdConfig_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toEtcdConfig())
''')
        assert output[-1] == '/port 8080'
