import re


def remove_cs_comments(csharp_code):
    # Remove single-line comments
    csharp_code = re.sub(r'//.*', '', csharp_code)

    # Remove multi-line comments
    csharp_code = re.sub(r'/\*.*?\*/', '', csharp_code, flags=re.DOTALL)

    return csharp_code


def count_lines_in_string(string):
    lines = string.splitlines()
    return len(lines)


def nb_lines_without_comments(file_path, remove_comments_func):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        str_without_comments = remove_comments_func(file.read())
        lines = str_without_comments.splitlines()
        filtered_lines = [line for line in lines if line.strip()]
        return len(filtered_lines)
