"""
Tests for dict .toCodeGuru2Config() method - format as CodeGuru config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeGuru2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeGuru2Config_basic(self):
        output = self._run('print({"repoArn": "arn:aws:codeguru"}.toCodeGuru2Config())')
        assert output[-1] == "repoArn = arn:aws:codeguru"

    def test_toCodeGuru2Config_multi(self):
        output = self._run('print({"repoArn": "arn:aws:codeguru", "type": "profiler"}.toCodeGuru2Config())')
        assert "repoArn = arn:aws:codeguru" in output[-1]
