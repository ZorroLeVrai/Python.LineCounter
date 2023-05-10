import os
from remove_comments import nb_lines_without_comments, remove_cs_comments

DIRECTORY_PATH = "D:/Users/Amine/Prgm/CSharp"
EXTENSION_LIST = ["cs", "sln"]


def count_line_in_file(file_path):
    '''
    Returns the number of lines contained in a given file
    '''
    # errors='ignore' to avoid having UnicodeDecodeError
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return len(file.readlines())


def find_cs_files(directory_path, lst_extension):
    '''
    This function takes as parameter a directory path
    It returns all *.cs in its directory and subdirectories
    '''
    ext_dico = {}  # Dictionary of extension to number of lines

    # Recursive function to search for *.cs files
    def search_cs_files(current_path):
        for file in os.listdir(current_path):
            file_path = os.path.join(current_path, file)
            if os.path.isfile(file_path):
                extension = next(
                    (ext for ext in lst_extension if file.endswith(f'.{ext}')), None)
                if extension is not None:
                    nb_lines = count_line_in_file(file_path)
                    # print(f"[{extension}]: {nb_lines} lines ")
                    if extension in ext_dico:
                        ext_dico[extension] += nb_lines
                    else:
                        ext_dico[extension] = nb_lines
            elif os.path.isdir(file_path):
                # Recursively search in subdirectories
                search_cs_files(file_path)

    search_cs_files(directory_path)
    return ext_dico


# Example usage
nb_lines_dico = find_cs_files(DIRECTORY_PATH, EXTENSION_LIST)
for extension, nb_lines in nb_lines_dico.items():
    print(f".{extension}: {nb_lines}")

# Test imported function
cs_file = "D:/Users/Amine/Prgm/CSharp/CalcApp/CalcLib/Tokenizer.cs"
nb_lines_in_cs_file = nb_lines_without_comments(cs_file, remove_cs_comments)
print("nb lines:", nb_lines_in_cs_file)
