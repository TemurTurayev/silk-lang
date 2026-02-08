"""
Tests for dict .toRekognitionConfig() method - format as Rekognition config.
"""

from silk.interpreter import Interpreter


class TestDictToRekognitionConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRekognitionConfig_basic(self):
        output = self._run('print({"collection": "faces"}.toRekognitionConfig())')
        assert output[-1] == "collection = faces"

    def test_toRekognitionConfig_multi(self):
        output = self._run('print({"confidence": 95, "maxFaces": 10}.toRekognitionConfig())')
        assert "confidence = 95" in output[-1]
