
class Stack:
    def __init__(self, *args):
        self.len = len(args)
        self.stack = list(args)

    def is_empty(self):
        if not self.len:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)
        self.len += 1

    def pop(self):
        if self.len:
            el = self.stack.pop()
            self.len -= 1
            return el
        else:
            raise IndexError('size = 0')

    def peek(self):
        if self.len:
            el = self.stack[-1]
            return el
        else:
            raise IndexError('size = 0')

    def size(self):
        return self.len

    def __str__(self):
        return str(self.stack)


bracket = {
        ')': '(',
        ']':'[',
        '}':'{'
    }
def check_brackets(brackets):
    if len(brackets) % 2 != 0:
        return False
    st = Stack()
    for s in brackets:
        if s in bracket:
            if st.size():
                top_el = st.pop()
                if bracket[s] != top_el:
                    return False
        else:
            st.push(s)
    return not st.size()














