"""
Tests for for..in iteration over dictionaries.
"""

from silk.interpreter import Interpreter


class TestForDict:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_for_key_in_dict(self):
        """Iterating over dict yields keys."""
        output = self._run('''
let m = {"a": 1, "b": 2}
let keys = []
for k in m {
    keys.push(k)
}
print(keys.length)
''')
        assert output[-1] == "2"

    def test_for_key_value_in_dict(self):
        """for k, v in dict iterates key-value pairs."""
        output = self._run('''
let m = {"x": 10, "y": 20}
let mut total = 0
for k, v in m {
    total += v
}
print(total)
''')
        assert output[-1] == "30"

    def test_for_dict_with_break(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let mut found = ""
for k, v in m {
    if v == 2 {
        found = k
        break
    }
}
print(found)
''')
        assert output[-1] == "b"

    def test_for_dict_empty(self):
        output = self._run('''
let mut count = 0
for k in {:} {
    count += 1
}
print(count)
''')
        assert output[-1] == "0"
