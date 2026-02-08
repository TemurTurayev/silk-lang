"""
Tests for dict .toDockerEnv() method - convert dict to Docker ENV format.
"""

from silk.interpreter import Interpreter


class TestDictToDockerEnv:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDockerEnv_basic(self):
        output = self._run('''
let d = {"PORT": 8080}
print(d.toDockerEnv())
''')
        assert output[-1] == 'ENV PORT=8080'

    def test_toDockerEnv_string(self):
        output = self._run('''
let d = {"APP_NAME": "silk"}
print(d.toDockerEnv())
''')
        assert output[-1] == 'ENV APP_NAME="silk"'
