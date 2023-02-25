def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size
print("File size in bytes of a plain file: ",file_size("book.txt"))
