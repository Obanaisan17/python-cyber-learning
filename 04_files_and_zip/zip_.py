from zipfile import ZipFile

list_file = ["File0", "file1", "file2", "file3", "test", "test/test.txt"]

'''with ZipFile("myzip.zip", "w") as z:
    for f in list_file:
        z.write(f)'''

with ZipFile("myzip.zip", "r") as z:
    z.printdir()
    z.extract("file2")
    print(z.read("test/test.txt"))
    z.extractall()
    print(z.infolist())
