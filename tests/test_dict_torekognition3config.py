"""
Tests for dict .toRekognition3Config() method - format as Rekognition v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRekognition3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRekognition3Config_basic(self):
        output = self._run('print({"collection": "faces"}.toRekognition3Config())')
        assert output[-1] == "collection = faces"

    def test_toRekognition3Config_multi(self):
        output = self._run('print({"collection": "faces", "threshold": 95}.toRekognition3Config())')
        assert output[-1] == "collection = faces\nthreshold = 95"
