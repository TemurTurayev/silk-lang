"""
Tests for dict .toDynamoDBConfig() method - DynamoDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToDynamoDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDynamoDBConfig_basic(self):
        output = self._run('''
let d = {"port": 8000}
print(d.toDynamoDBConfig())
''')
        assert output[-1] == 'port = 8000'

    def test_toDynamoDBConfig_string(self):
        output = self._run('''
let d = {"region": "us-east-1"}
print(d.toDynamoDBConfig())
''')
        assert output[-1] == 'region = us-east-1'
