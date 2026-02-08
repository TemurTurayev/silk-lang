"""
Tests for dict .toTerraformHCL() method - convert dict to Terraform HCL format.
"""

from silk.interpreter import Interpreter


class TestDictToTerraformHCL:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTerraformHCL_string(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toTerraformHCL())
''')
        assert output[-1] == 'name = "Bob"'

    def test_toTerraformHCL_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toTerraformHCL())
''')
        assert output[-1] == 'port = 8080'
