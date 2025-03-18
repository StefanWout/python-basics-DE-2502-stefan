from pathlib import Path

cwd = Path.cwd()

demo_file_path = cwd / 'demo_files' / 'my_data.txt'

file = open(demo_file_path)

print(demo_file_path)