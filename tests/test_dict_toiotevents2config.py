"""
Tests for dict .toIoTEvents2Config() method - format as IoT Events config.
"""

from silk.interpreter import Interpreter


class TestDictToIoTEvents2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toIoTEvents2Config_basic(self):
        output = self._run('print({"detectorName": "temp-alert"}.toIoTEvents2Config())')
        assert output[-1] == "detectorName = temp-alert"

    def test_toIoTEvents2Config_multi(self):
        output = self._run('print({"detectorName": "temp-alert", "key": "deviceId"}.toIoTEvents2Config())')
        assert "detectorName = temp-alert" in output[-1]
