import os

def get_file_tree(path='.', prefix=''):
    tree_lines = []
    entries = sorted(os.listdir(path))
    files = [f for f in entries if os.path.isfile(os.path.join(path, f))]

    for i, file in enumerate(files):
        connector = '└── ' if i == len(files) - 1 else '├── '
        tree_lines.append(prefix + connector + file)

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            sub_prefix = prefix + ('    ')
            tree_lines += get_file_tree(full_path, sub_prefix)

    return tree_lines

tree_lines = get_file_tree()
tree_str = "\n".join(tree_lines)

# Write to README.md
with open("README.md", "a") as readme:
    readme.write("\n## 📁 File Tree\n\n```text\n")
    readme.write(tree_str)
    readme.write("\n```\n")
