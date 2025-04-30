# import os

# def get_file_tree(path='.', prefix=''):
#     tree_lines = []
#     entries = sorted(os.listdir(path))
#     print(entries)
#     files = [f for f in entries if os.path.isfile(os.path.join(path, f))]

#     for i, file in enumerate(files):
#         connector = '└── ' if i == len(files) - 1 else '├── '
#         tree_lines.append(prefix + connector + file)

#     for entry in entries:
#         full_path = os.path.join(path, entry)
#         if os.path.isdir(full_path):
#             sub_prefix = prefix + ('    ')
#             tree_lines += get_file_tree(full_path, sub_prefix)

#     return tree_lines




# print("Hello")
# tree_lines = get_file_tree()
# tree_str = "\n".join(tree_lines)

# # Write to README.md
# with open("README.md", "a") as readme:
#     readme.write("\n##  File Tree\n\n```text\n")
#     readme.write(tree_str)
#     readme.write("\n```\n")
import os

def get_top_level_files(path='.'):
    files = sorted(f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)))
    tree_lines = [f"├── {file}" for file in files]
    return "\n".join(tree_lines)

tree_output = get_top_level_files()
print(tree_output)

# Append to README.md
with open("README.md", "w+", encoding="utf-8") as readme:
    readme.write("\n##  Files in Current Directory\n\n```text\n")
    readme.write(tree_output)
    readme.write("\n```\n")
