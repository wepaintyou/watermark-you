from pathlib import Path
import git
import os

ROOT_DIR = str(Path(git.Repo(".", search_parent_directories=True).working_tree_dir))
DEFAULT_WATERMARK_IMAGE_PATH = os.path.join(
    ROOT_DIR, "data/images/default_watermark.png"
)
DEFAULT_TEST_IMAGE_PATH = os.path.join(ROOT_DIR, "data/images/default_test_image.png")