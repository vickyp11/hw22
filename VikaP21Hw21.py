#task1
"""
Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method, which has to cover all the requirements to context managers mentioned here:
"""
import logging

class FileManager:
    counter = 0
    log_message = ''

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    @classmethod
    def get_num_cls_usage(cls):
        return cls.counter

    def __enter__(self):
        FileManager.counter += 1
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        FileManager.log_message = logging.info('The class was used.')
        self.opening = open(self.name, self.mode)
        #print(1 + 'a')
        return self.opening

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Number of class usages:', FileManager.get_num_cls_usage())
        self.opening.close()
        return True

#
# with FileManager('homework.log', 'r') as file:
#     print(file.read())
#
# with FileManager('homework.log', 'r') as file:
#     print(file.read())
#
# with FileManager('homework.log', 'r') as file:
#     print(file.read())




