from pathlib import Path
import git

ROOT_DIR = str(Path(git.Repo(".", search_parent_directories=True).working_tree_dir))
