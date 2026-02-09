"""
Tests for dict .toHealthLake2Config() method - format as HealthLake v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToHealthLake2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHealthLake2Config_basic(self):
        output = self._run('print({"datastore": "clinical"}.toHealthLake2Config())')
        assert output[-1] == "datastore = clinical"

    def test_toHealthLake2Config_multi(self):
        output = self._run('print({"datastore": "clinical", "format": "FHIR"}.toHealthLake2Config())')
        assert output[-1] == "datastore = clinical\nformat = FHIR"
