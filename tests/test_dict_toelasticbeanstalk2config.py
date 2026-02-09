"""
Tests for dict .toElasticBeanstalk2Config() method - format as ElasticBeanstalk v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToElasticBeanstalk2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toElasticBeanstalk2Config_basic(self):
        output = self._run('print({"platform": "python"}.toElasticBeanstalk2Config())')
        assert output[-1] == "platform = python"

    def test_toElasticBeanstalk2Config_multi(self):
        output = self._run('print({"platform": "python", "tier": "web"}.toElasticBeanstalk2Config())')
        assert output[-1] == "platform = python\ntier = web"
