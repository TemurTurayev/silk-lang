"""
Tests for dict .toKubernetesYAML() method - Kubernetes YAML-like format.
"""

from silk.interpreter import Interpreter


class TestDictToKubernetesYAML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKubernetesYAML_basic(self):
        output = self._run('''
let d = {"apiVersion": "v1"}
print(d.toKubernetesYAML())
''')
        assert output[-1] == 'apiVersion: v1'

    def test_toKubernetesYAML_number(self):
        output = self._run('''
let d = {"replicas": 3}
print(d.toKubernetesYAML())
''')
        assert output[-1] == 'replicas: 3'
