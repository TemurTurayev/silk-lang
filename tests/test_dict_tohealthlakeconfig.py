"""
Tests for dict .toHealthLakeConfig() method - format as HealthLake config.
"""

from silk.interpreter import Interpreter


class TestDictToHealthLakeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHealthLakeConfig_basic(self):
        output = self._run('print({"datastore": "fhir_store"}.toHealthLakeConfig())')
        assert output[-1] == "datastore = fhir_store"

    def test_toHealthLakeConfig_multi(self):
        output = self._run('print({"version": "R4", "preload": true}.toHealthLakeConfig())')
        assert "version = R4" in output[-1]
