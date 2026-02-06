"""
Tests for compound assignment on members and indices.

Syntax:
  obj.field += value
  arr[i] += value
"""

from silk.interpreter import Interpreter


class TestCompoundMemberAssign:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_member_plus_assign(self):
        output = self._run('''
struct Counter { count }
let mut c = Counter { count: 10 }
c.count += 5
print(c.count)
''')
        assert output[-1] == "15"

    def test_member_minus_assign(self):
        output = self._run('''
struct Score { value }
let mut s = Score { value: 100 }
s.value -= 30
print(s.value)
''')
        assert output[-1] == "70"

    def test_member_star_assign(self):
        output = self._run('''
struct Factor { n }
let mut f = Factor { n: 5 }
f.n *= 3
print(f.n)
''')
        assert output[-1] == "15"

    def test_member_slash_assign(self):
        output = self._run('''
struct Half { val }
let mut h = Half { val: 20 }
h.val /= 4
print(h.val)
''')
        assert output[-1] == "5"


class TestCompoundIndexAssign:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_index_plus_assign(self):
        output = self._run('''
let mut arr = [1, 2, 3]
arr[0] += 10
print(arr)
''')
        assert output[-1] == "[11, 2, 3]"

    def test_index_minus_assign(self):
        output = self._run('''
let mut arr = [10, 20, 30]
arr[1] -= 5
print(arr[1])
''')
        assert output[-1] == "15"

    def test_map_plus_assign(self):
        output = self._run('''
let mut m = {"score": 10}
m["score"] += 5
print(m["score"])
''')
        assert output[-1] == "15"

    def test_map_string_concat_assign(self):
        output = self._run('''
let mut m = {"name": "Hello"}
m["name"] += " World"
print(m["name"])
''')
        assert output[-1] == "Hello World"
