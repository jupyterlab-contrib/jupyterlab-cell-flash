"""
jupyterlab-cell-flash setup
"""
import json
from pathlib import Path

import setuptools

HERE = Path(__file__).parent.resolve()

# The name of the project
NAME = "jupyterlab-cell-flash"
PACKAGE = NAME.replace("-", "_")

lab_path = HERE / PACKAGE / "labextension"

# Representative files that should exist after a successful build
ensured_targets = [
    str(lab_path / "package.json"),
    str(lab_path / "static" / "style.js"),
]

labext_name = "jupyterlab-cell-flash"

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
]

# Get the package info from package.json
pkg_json = json.loads((HERE / "package.json").read_bytes())

try:
    from jupyter_packaging import wrap_installers, npm_builder, get_data_files

    # In develop mode, just run yarn
    builder = npm_builder(build_cmd="build", build_dir=lab_path, source_dir="src")
    cmdclass = wrap_installers(post_develop=builder, ensured_targets=ensured_targets)

    setup_args = dict(
        cmdclass=cmdclass,
        data_files=get_data_files(data_files_spec),
    )
except ImportError:
    setup_args = dict()

setup_args["version"] = pkg_json["version"]

if __name__ == "__main__":
    setuptools.setup(**setup_args)
