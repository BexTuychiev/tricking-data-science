from joblib import Parallel, delayed
from rich.progress import track
import json
import glob
import re


def replace_i(notebook_path):
    """
    A function to replace "ı"s with "i" in a Jupyter Notebook.
    """

    with open(notebook_path, "r") as file:
        data = file.read()

    with open(notebook_path, "w") as file:
        data = data.replace("ı", "i")
        file.write(data)


if __name__ == "__main__":
    notebooks = glob.glob("*/*.ipynb")
    Parallel(n_jobs=10, backend="multiprocessing")(
        delayed(replace_i)(path) for path in track(notebooks)
    )
