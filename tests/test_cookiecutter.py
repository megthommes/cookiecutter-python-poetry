from __future__ import annotations

import subprocess
from pathlib import Path
from pytest_cookies import Cookies

from tests.utils import (
    file_contains_text,
    is_valid_yaml,
    run_within_dir,
    assert_project_created,
    assert_project_path,
    assert_file_exists,
    assert_file_not_exists,
)


def test_bake_project(cookies: Cookies) -> None:
    """Test baking a project with default configuration."""
    result = cookies.bake(extra_context={"project_name": "my-project"})
    assert_project_created(result)
    assert_project_path(result, "my-project")


def test_using_pytest(cookies: Cookies, tmp_path: Path) -> None:
    """Test that the project is created and tests pass when using pytest."""
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert_project_created(result)
        assert_project_path(result, "example-project")
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

        # Install and test with poetry
        project_path = result.project_path
        with run_within_dir(project_path):
            assert subprocess.check_call(["poetry", "install", "--no-interaction"]) == 0
            assert subprocess.check_call(["poetry", "run", "make", "test"]) == 0


def test_devcontainer(cookies: Cookies, tmp_path: Path) -> None:
    """Test creation of devcontainer files with devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert_project_created(result)
        assert_file_exists(result.project_path / ".devcontainer" / "devcontainer.json")
        assert_file_exists(result.project_path / ".devcontainer" / "postCreateCommand.sh")


def test_not_devcontainer(cookies: Cookies, tmp_path: Path) -> None:
    """Test absence of devcontainer files with devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert_project_created(result)
        assert_file_not_exists(result.project_path / ".devcontainer" / "devcontainer.json")
        assert_file_not_exists(result.project_path / ".devcontainer" / "postCreateCommand.sh")


def test_cicd_contains_artifactory_secrets(cookies: Cookies, tmp_path: Path) -> None:
    """Test CI/CD configuration includes Artifactory secrets"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "artifactory"})
        assert_project_created(result)
        workflow_path = result.project_path / ".github" / "workflows" / "on-release-main.yml"
        assert is_valid_yaml(workflow_path)
        for text in ["ARTIFACTORY_URL", "ARTIFACTORY_USERNAME", "ARTIFACTORY_PASSWORD"]:
            assert file_contains_text(workflow_path, text)
        assert file_contains_text(result.project_path / "Makefile", "build-and-publish")


def test_cicd_contains_pypi_secrets(cookies: Cookies, tmp_path: Path) -> None:
    """Test CI/CD configuration includes PyPI secrets"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "pypi"})
        assert_project_created(result)
        workflow_path = result.project_path / ".github" / "workflows" / "on-release-main.yml"
        assert is_valid_yaml(workflow_path)
        assert file_contains_text(workflow_path, "PYPI_TOKEN")
        assert file_contains_text(result.project_path / "Makefile", "build-and-publish")


def test_dont_publish(cookies: Cookies, tmp_path: Path) -> None:
    """Test no publish when publish_to=none"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none"})
        assert_project_created(result)
        workflow_path = result.project_path / ".github" / "workflows" / "on-release-main.yml"
        assert is_valid_yaml(workflow_path)
        assert not file_contains_text(workflow_path, "make build-and-publish")


def test_mkdocs(cookies: Cookies, tmp_path: Path) -> None:
    """Test MkDocs setup when mkdocs=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "y"})
        assert_project_created(result)
        workflow_path_main = result.project_path / ".github" / "workflows" / "main.yml"
        workflow_path_release = result.project_path / ".github" / "workflows" / "on-release-main.yml"
        assert is_valid_yaml(workflow_path_main)
        assert is_valid_yaml(workflow_path_release)
        assert file_contains_text(workflow_path_release, "mkdocs gh-deploy")
        assert file_contains_text(result.project_path / "Makefile", "docs:")
        assert (result.project_path / "docs").is_dir()


def test_not_mkdocs(cookies: Cookies, tmp_path: Path) -> None:
    """Test absence of MkDocs setup when mkdocs=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "n"})
        assert_project_created(result)
        workflow_path_main = result.project_path / ".github" / "workflows" / "main.yml"
        workflow_path_release = result.project_path / ".github" / "workflows" / "on-release-main.yml"
        assert is_valid_yaml(workflow_path_main)
        assert is_valid_yaml(workflow_path_release)
        assert not file_contains_text(workflow_path_release, "mkdocs gh-deploy")
        assert not file_contains_text(result.project_path / "Makefile", "docs:")
        assert not (result.project_path / "docs").is_dir()


def test_tox(cookies: Cookies, tmp_path: Path) -> None:
    """Test Tox configuration"""
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert_project_created(result)
        assert_file_exists(result.project_path / "tox.ini")
        assert file_contains_text(result.project_path / "tox.ini", "[tox]")


def test_dockerfile(cookies: Cookies, tmp_path: Path) -> None:
    """Test Dockerfile creation with dockerfile=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert_project_created(result)
        assert_file_exists(result.project_path / "Dockerfile")


def test_not_dockerfile(cookies: Cookies, tmp_path: Path) -> None:
    """Test absence of Dockerfile with dockerfile=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert_project_created(result)
        assert_file_not_exists(result.project_path / "Dockerfile")


def test_codecov(cookies: Cookies, tmp_path: Path) -> None:
    """Test Codecov configuration when codecov=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert_project_created(result)
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert_file_exists(result.project_path / "codecov.yaml")
        assert_file_exists(result.project_path / ".github" / "workflows" / "validate-codecov-config.yml")


def test_not_codecov(cookies: Cookies, tmp_path: Path) -> None:
    """Test absence of Codecov configuration when codecov=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"codecov": "n"})
        assert_project_created(result)
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert_file_not_exists(result.project_path / "codecov.yaml")
        assert_file_not_exists(result.project_path / ".github" / "workflows" / "validate-codecov-config.yml")


def test_remove_release_workflow(cookies: Cookies, tmp_path: Path) -> None:
    """Test removal of release workflow based on configuration"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none", "mkdocs": "y"})
        assert_project_created(result)
        assert_file_exists(result.project_path / ".github" / "workflows" / "on-release-main.yml")

        result = cookies.bake(extra_context={"publish_to": "none", "mkdocs": "n"})
        assert_project_created(result)
        assert_file_not_exists(result.project_path / ".github" / "workflows" / "on-release-main.yml")
