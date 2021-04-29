# supporting with statement with user defined object

class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# using with statement with MessageWriter


with MessageWriter('util/sample_write_file.txt') as xfile:
    xfile.write('using user defined object with "with"')


# with MessageWriter('util/sample_write_file.txt') as xfile:
#     xfile.write("using user defined object")
