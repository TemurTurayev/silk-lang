"""
Tests for dict .toElasticBeanstalkConfig() method - format as AWS Elastic Beanstalk config.
"""

from silk.interpreter import Interpreter


class TestDictToElasticBeanstalkConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElasticBeanstalkConfig_basic(self):
        output = self._run('print({"env": "production"}.toElasticBeanstalkConfig())')
        assert output[-1] == "env = production"

    def test_toElasticBeanstalkConfig_multi(self):
        output = self._run('print({"env": "production", "tier": "web"}.toElasticBeanstalkConfig())')
        assert "env = production" in output[-1]
