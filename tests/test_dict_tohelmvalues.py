"""
Tests for dict .toHelmValues() method - convert dict to Helm values.yaml format.
"""

from silk.interpreter import Interpreter


class TestDictToHelmValues:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHelmValues_basic(self):
        output = self._run('''
let d = {"replicaCount": 3}
print(d.toHelmValues())
''')
        assert output[-1] == 'replicaCount: 3'

    def test_toHelmValues_string(self):
        output = self._run('''
let d = {"image": "nginx"}
print(d.toHelmValues())
''')
        assert output[-1] == 'image: "nginx"'
