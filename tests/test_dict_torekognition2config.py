"""
Tests for dict .toRekognition2Config() method - format as Rekognition v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRekognition2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRekognition2Config_basic(self):
        output = self._run('print({"collection": "faces"}.toRekognition2Config())')
        assert output[-1] == "collection = faces"

    def test_toRekognition2Config_multi(self):
        output = self._run('print({"collection": "faces", "confidence": 95}.toRekognition2Config())')
        assert output[-1] == "collection = faces\nconfidence = 95"
