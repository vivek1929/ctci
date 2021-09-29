# How could you use a single array to implement three stacks.

import copy

class MultiStack:

    def __init__(self, stacks) -> None:
        self.values = list()
        self.indexes = dict()
        self.sizes = dict()
        self.stacks = stacks

    def push(self, stack_no, data):
        if f'stack{stack_no}' not in self.indexes:
            self.values.append(data)
            self.indexes[f'stack{stack_no}'] = len(self.values)-1
            self.sizes[f'stack{stack_no}'] = 1
            return
        
        current_index = self.indexes[f'stack{stack_no}']
        current_size = self.sizes[f'stack{stack_no}']
        space_available = self.check_if_space_available(current_index+1, stack_no)
        if space_available:
            if len(self.values) > current_index+current_size:
                self.values[current_index+1] = data
            else:
                self.values.append(data)
        self.sizes[f'stack{stack_no}'] += 1

    def pop(self, stack_no):
        if f'stack{stack_no}' not in self.indexes:
            raise Exception('Stack was never created')
        
        if self.sizes[f'stack{stack_no}'] == 0:
            raise Exception('Stack is empty')

        return self.values.pop(self.indexes[f'stack{stack_no}'] + self.sizes[f'stack{stack_no}']-1)

    def size(self, stack_no):
        return self.sizes[f'stack{stack_no}']

    def check_if_space_available(self, index, stack_no):
        space_available = True
        for each in self.indexes:
            if each != f'stack{stack_no}':
                if index >= self.indexes[each]:
                    self.values = shift_values_right(self.values, index)

def shift_values_right(values, index):
    values.add(None)
    for each in range(index, len(values)):
        values[each] = values[each+1]



if __name__ == '__main__':
    new_stacker = MultiStack(3)
    new_stacker.push(1, 'a')
    new_stacker.push(1, 'b')
    new_stacker.push(1, 'c')

    print(new_stacker.size(1))

    print(new_stacker.pop(1))