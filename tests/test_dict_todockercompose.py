"""
Tests for dict .toDockerCompose() method - convert dict to Docker Compose format.
"""

from silk.interpreter import Interpreter


class TestDictToDockerCompose:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDockerCompose_basic(self):
        output = self._run('''
let d = {"image": "nginx"}
print(d.toDockerCompose())
''')
        assert output[-1] == 'image: nginx'

    def test_toDockerCompose_number(self):
        output = self._run('''
let d = {"replicas": 3}
print(d.toDockerCompose())
''')
        assert output[-1] == 'replicas: 3'
