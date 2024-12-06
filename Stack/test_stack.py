import pytest

from stack import Stack


class TestStack:
    def setup_method(self):
        self.stack1 = Stack()
        self.stack2 = Stack(1,2,3,4,5,6,9)

    def teardown_method(self):
        del self.stack1
        del self.stack2

    def test_is_empty(self):
        empty_true = self.stack1.is_empty()
        empty_false = self.stack2.is_empty()
        assert empty_true == True
        assert empty_false == False


    def test_push_to_empty_stack(self):
        self.stack1.push(15)
        assert self.stack1.__str__() == '[15]'

    def test_push_to_stack(self):
        self.stack2.push(15)
        assert self.stack2.__str__() == Stack(1,2,3,4,5,6,9,15).__str__()

    def test_size(self):
        assert self.stack1.size() == 0
        assert  self.stack2.size() == 7

    def test_pop_from_empty_stack(self):
        with pytest.raises(IndexError):
            self.stack1.pop()

    def test_pop_from_stack(self):
        el = self.stack2.pop()
        assert el == 9
        assert self.stack2.__str__() == Stack(1,2,3,4,5,6).__str__()

    def test_size_after_pop_and_push(self):
        size_before_pop = self.stack2.size()
        self.stack2.pop()
        size_after_pop = self.stack2.size()
        assert size_before_pop - size_after_pop == 1
        size_before_push = self.stack2.size()
        self.stack2.push(10)
        size_after_push = self.stack2.size()
        assert size_after_push - size_before_push == 1

    def test_peek_in_empty_stack(self):
        with pytest.raises(IndexError):
            self.stack1.peek()

    def test_peek_in_stack(self):
        size = self.stack2.size()
        el = self.stack2.peek()
        assert el == 9
        assert size == self.stack2.size()




