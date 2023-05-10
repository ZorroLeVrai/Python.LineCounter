# Line counter for programs
A very simple program to get the number of lines contained in a given directory for each file extension.
Counting the number of lines is done recursively in sub-folders.

**Example of usage**
```
DIRECTORY_PATH = "D:/Users/Root/Prgm"
EXTENSION_LIST = ["cs", "js"]
#The find_cs_files returns a dico
nb_lines_dico = find_cs_files(DIRECTORY_PATH, EXTENSION_LIST)
for extension, nb_lines in nb_lines_dico.items():
    print(f".{extension}: {nb_lines}")
```