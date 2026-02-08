"""
Tests for dict .toCloudTrail2Config() method - format as CloudTrail config.
"""

from silk.interpreter import Interpreter


class TestDictToCloudTrail2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCloudTrail2Config_basic(self):
        output = self._run('print({"trailName": "main-trail"}.toCloudTrail2Config())')
        assert output[-1] == "trailName = main-trail"

    def test_toCloudTrail2Config_multi(self):
        output = self._run('print({"trailName": "main-trail", "isMultiRegion": true}.toCloudTrail2Config())')
        assert "trailName = main-trail" in output[-1]
