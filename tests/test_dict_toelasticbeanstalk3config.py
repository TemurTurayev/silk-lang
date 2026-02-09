"""
Tests for dict .toElasticBeanstalk3Config() method - format dict as ElasticBeanstalk3 config.
"""

from silk.interpreter import Interpreter


class TestDictToElasticBeanstalk3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElasticBeanstalk3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toElasticBeanstalk3Config())')
        assert output[-1] == "host = localhost"

    def test_toElasticBeanstalk3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toElasticBeanstalk3Config())')
        assert output[-1] == "host = localhost\nport = 443"
