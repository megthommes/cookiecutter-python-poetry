#!/usr/bin/env python
from __future__ import annotations

from pathlib import Path
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove a file from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    """Remove a directory from the project directory."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    # github actions
    if "{{cookiecutter.include_github_actions}}" != "y":
        # if not using GitHub Actions, remove the .github directory
        remove_dir(".github")
    else:
        # if using GitHub Actions, remove the workflows that are not needed
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to}}" == "none":
            remove_file(".github/workflows/on-release-main.yml")

    # publish_to

    # mkdocs
    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    # codecov
    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    # dockerfile
    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    # devcontainer
    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")
