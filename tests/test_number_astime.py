"""
Tests for number .asTime() method.
"""

from silk.interpreter import Interpreter


class TestNumberAsTime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_asTime_minutes(self):
        output = self._run('print(125.asTime())')
        assert output[-1] == "2:05"

    def test_asTime_hours(self):
        output = self._run('print(3661.asTime())')
        assert output[-1] == "1:01:01"

    def test_asTime_zero(self):
        output = self._run('print(0.asTime())')
        assert output[-1] == "0:00"
