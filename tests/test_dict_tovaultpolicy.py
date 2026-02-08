"""
Tests for dict .toVaultPolicy() method - convert dict to HashiCorp Vault policy format.
"""

from silk.interpreter import Interpreter


class TestDictToVaultPolicy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVaultPolicy_basic(self):
        output = self._run('''
let d = {"path": "secret/data"}
print(d.toVaultPolicy())
''')
        assert output[-1] == 'path = "secret/data"'

    def test_toVaultPolicy_number(self):
        output = self._run('''
let d = {"max_ttl": 3600}
print(d.toVaultPolicy())
''')
        assert output[-1] == 'max_ttl = 3600'
