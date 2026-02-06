"""
Tests for guard statement (early return).
guard condition else { body }
"""

from silk.interpreter import Interpreter


class TestGuard:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_guard_passes(self):
        output = self._run('''
fn check(x) {
    guard x > 0 else {
        return "negative"
    }
    return "positive"
}
print(check(5))
''')
        assert output[-1] == "positive"

    def test_guard_fails(self):
        output = self._run('''
fn check(x) {
    guard x > 0 else {
        return "negative"
    }
    return "positive"
}
print(check(-1))
''')
        assert output[-1] == "negative"

    def test_guard_multiple(self):
        output = self._run('''
fn validate(name, age) {
    guard name.length > 0 else {
        return "empty name"
    }
    guard age >= 18 else {
        return "too young"
    }
    return "valid"
}
print(validate("Alice", 20))
print(validate("", 20))
print(validate("Bob", 15))
''')
        assert output[-3] == "valid"
        assert output[-2] == "empty name"
        assert output[-1] == "too young"
