"""
Tests for dict .toAnsibleYAML() method - convert dict to Ansible YAML task format.
"""

from silk.interpreter import Interpreter


class TestDictToAnsibleYAML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAnsibleYAML_basic(self):
        output = self._run('''
let d = {"name": "Install nginx"}
print(d.toAnsibleYAML())
''')
        assert output[-1] == '- name: Install nginx'

    def test_toAnsibleYAML_number(self):
        output = self._run('''
let d = {"port": 80}
print(d.toAnsibleYAML())
''')
        assert output[-1] == '- port: 80'
