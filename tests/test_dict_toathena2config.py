"""
Tests for dict .toAthena2Config() method - format as Athena config.
"""

from silk.interpreter import Interpreter


class TestDictToAthena2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAthena2Config_basic(self):
        output = self._run('print({"database": "my_db"}.toAthena2Config())')
        assert output[-1] == "database = my_db"

    def test_toAthena2Config_multi(self):
        output = self._run('print({"database": "my_db", "outputLocation": "s3://bucket/"}.toAthena2Config())')
        assert "database = my_db" in output[-1]
