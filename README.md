# cookiecutter-python-poetry

<!-- badges-begin -->

[![Status][badge-status]][badge-status]
[![Python Version][badge-python-version]][github-repo]
[![CalVer][badge-calver]][calver]
[![License][badge-license]][license]<br>
[![Read the documentation][badge-readthedocs-repo]][readthedocs-repo]
[![Tests][badge-github-actions-repo]][github-actions-repo]
[![Codecov][badge-codecov]][codecov]<br>
[![pre-commit enabled][badge-pre-commit]][pre-commit]
[![Black codestyle][badge-black]][black]

<!-- badges-end -->

[Cookiecutter] template for a Python project with all the necessary tools for development, testing, and deployment. Based on [cookiecutter-hypermodern-python], [cookiecutter-poetry], and [cookiecutter-pypackage].

✨📚✨ [Read the full documentation][readthedocs-repo]

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- CI/CD with [GitHub Actions][github-actions]
- Pre-commit hooks with [pre-commit]
- Test automation with [Nox]
- Linting with [pre-commit] and [Flake8]
- Code formatting with [Black] and [Prettier]
- Import sorting with [isort]
- Automated dependency updates with [Dependabot]
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Documentation with [Read the Docs][read-the-docs]
- Publishing to [PyPI] / [TestPyPI] or [Artifactory] by creating a new release on GitHub
- Automated release notes with [Release Drafter][release-drafter]
- Static type-checking with [mypy]
- Runtime type-checking with [Typeguard]
- Automated Python syntax upgrades with [pyupgrade]
- Security audit with [Bandit] and [Safety]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Manage project labels with [GitHub Labeler][github-labeler]
- Compatibility testing for multiple versions of Python with [Tox]
- Containerization with [Docker]
- Development environment with [VSCode devcontainers][devcontainers]

<!-- features-end -->

<!-- urls-begin -->
<!-- features -->
[artifactory]: https://jfrog.com/artifactory
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[calver]: http://calver.org/
[codecov]: https://codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[devcontainers]: https://code.visualstudio.com/docs/devcontainers/containers
[docker]: https://www.docker.com
[flake8]: http://flake8.pycqa.org
[github-actions]: https://github.com/features/actions
[github-labeler]: https://github.com/marketplace/actions/github-labeler
[isort]: https://pycqa.github.io/isort/
[mypy]: https://mypy.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read-the-docs]: https://readthedocs.org/
[release-drafter]: https://github.com/release-drafter/release-drafter
[safety]: https://github.com/pyupio/safety
[testpypi]: https://test.pypi.org/
[tox]: https://tox.wiki/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
<!-- cookiecutter-python-poetry -->
[codecov]: https://codecov.io/gh/megthommes/cookiecutter-python-poetry-instance
[github-actions-repo]: https://github.com/megthommes/cookiecutter-python-poetry/actions?workflow=Tests
[license]: https://opensource.org/licenses/MIT
[readthedocs-repo]: https://cookiecutter-python-poetry.readthedocs.io/
[github-repo]: https://github.com/megthommes/cookiecutter-python-poetry
[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter-hypermodern-python]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[cookiecutter-poetry]: https://github.com/fpgmaas/cookiecutter-poetry
[cookiecutter-pypackage]: https://github.com/Nekroze/cookiecutter-pypackage/
<!-- badges -->
[badge-black]: https://img.shields.io/badge/code%20style-black-000000.svg
[badge-calver]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[badge-codecov]: https://codecov.io/gh/megthommes/cookiecutter-python-poetry-instance/branch/main/graph/badge.svg
[badge-github-actions-repo]: https://github.com/megthommes/cookiecutter-python-poetry/workflows/Tests/badge.svg
[badge-license]: https://img.shields.io/github/license/megthommes/cookiecutter-python-poetry
[badge-pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[badge-python-version]: https://img.shields.io/pypi/pyversions/cookiecutter-python-poetry-instance
[badge-readthedocs-repo]: https://img.shields.io/readthedocs/cookiecutter-python-poetry/latest.svg?label=Read%20the%20Docs
[badge-status]: https://badgen.net/badge/status/alpha/d8624d
<!-- urls-end -->