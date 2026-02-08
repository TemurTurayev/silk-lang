"""
Tests for dict .toCURConfig() method - format as Cost and Usage Report config.
"""

from silk.interpreter import Interpreter


class TestDictToCURConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCURConfig_basic(self):
        output = self._run('print({"report": "monthly-cost"}.toCURConfig())')
        assert output[-1] == "report = monthly-cost"

    def test_toCURConfig_multi(self):
        output = self._run('print({"format": "parquet", "bucket": "reports"}.toCURConfig())')
        assert "format = parquet" in output[-1]
