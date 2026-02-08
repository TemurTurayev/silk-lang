"""
Tests for dict .toKafkaConfig() method - Kafka config format.
"""

from silk.interpreter import Interpreter


class TestDictToKafkaConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKafkaConfig_basic(self):
        output = self._run('''
let d = {"bootstrap.servers": "localhost:9092"}
print(d.toKafkaConfig())
''')
        assert output[-1] == 'bootstrap.servers=localhost:9092'

    def test_toKafkaConfig_number(self):
        output = self._run('''
let d = {"max.poll.records": 500}
print(d.toKafkaConfig())
''')
        assert output[-1] == 'max.poll.records=500'
