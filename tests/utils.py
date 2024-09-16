from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path
from typing import Generator
from pytest_cookies import Result

import yaml


def is_valid_yaml(path: str | Path) -> bool:
    """
    Check if a file exists and is a valid YAML file.

    Parameters
    ----------
    path : str | Path
        Path to the file to check.

    Returns
    -------
    bool
        True if the file exists and is a valid YAML file, False otherwise.
    """
    path = Path(path)

    if not path.is_file():
        print(f"File does not exist: {path}")
        return False

    try:
        with path.open("r") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {path} - Error: {e}")
        return False
    except OSError as e:
        print(f"Error reading file: {path} - Error: {e}")
        return False

    return True


@contextmanager
def run_within_dir(path: str) -> Generator[None, None, None]:
    """
    Run a block of code within a specific directory.

    Parameters
    ----------
    path : str
        Path to the directory to run the code in.

    Yields
    ------
    None
        This context manager yields control to the code block within the specified directory.
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    """
    Check if a file contains a specific text.

    Parameters
    ----------
    file : str
        Path to the file to check.
    text : str
        Text to search for in the file.

    Returns
    -------
    bool
        True if the file contains the text, False otherwise.
    """
    with open(file) as f:
        return f.read().find(text) != -1


def assert_project_created(result: Result) -> None:
    """
    Helper function to assert that the cookiecutter project was created.

    Parameters
    ----------
    result : Result
        The cookiecutter result to check.

    Returns
    -------
    None
    """
    assert result.exit_code == 0
    assert result.exception is None


def assert_file_exists(file_path: Path) -> None:
    """
    Helper function to assert that a file exists.

    Parameters
    ----------
    file_path : Path
        The path to the file to check.
    """
    assert file_path.is_file()


def assert_file_not_exists(file_path: Path) -> None:
    """
    Helper function to assert that a file does not exist.

    Parameters
    ----------
    file_path : Path
        The path to the file to check.
    """
    assert not file_path.is_file()


def assert_project_path(result: Result, expected_name: str) -> None:
    """
    Helper function to assert the project path's name and existence.

    Parameters
    ----------
    result : Result
        The cookiecutter result to check.
    expected_name : str
        The expected name of the project path.
    """
    assert result.project_path.name == expected_name
    assert result.project_path.is_dir()
