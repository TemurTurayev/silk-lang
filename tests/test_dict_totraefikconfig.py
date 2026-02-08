"""
Tests for dict .toTraefikConfig() method - Traefik config format.
"""

from silk.interpreter import Interpreter


class TestDictToTraefikConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTraefikConfig_basic(self):
        output = self._run('''
let d = {"entrypoint": "web"}
print(d.toTraefikConfig())
''')
        assert output[-1] == '[entrypoint]\n  value = "web"'

    def test_toTraefikConfig_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toTraefikConfig())
''')
        assert output[-1] == '[port]\n  value = 8080'
