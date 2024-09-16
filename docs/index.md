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

An example of a repository generated with this package can be found [here][github-repo-example].

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

## Quickstart

<!-- quickstart-begin -->

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

```bash
pip install cookiecutter-python-poetry
ccpp
```

Alternatively, [install `cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) and directly pass the URL to this
GitHub repository to the `cookiecutter` command:

```bash
cookiecutter https://github.com/megthommes/cookiecutter-python-poetry.git
```

Create a repository on GitHub, and then run the following commands, replacing `<project-name>`, with the name that you gave the Github repository and
`<github_author_handle>` with your Github username.

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](./features/publishing.md#set-up-for-pypi).

For activating the automatic documentation with MkDocs, see [here](./features/mkdocs.md#enabling-the-documentation-on-github).

To enable the code coverage reports, see [here](./features/codecov).

<!-- quickstart-end -->

## Releasing

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using [poetry version](https://python-poetry.org/docs/cli/#version).
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

The Release workflow performs the following automated steps:

- Build and upload the package to PyPI or Artifactory.
- Apply a version tag to the repository.
- Publish a GitHub Release.

Release notes are populated with the titles and authors of merged pull requests.

You can group the pull requests into separate sections
by applying labels to them, like this:

<!-- table-release-drafter-sections-begin -->

| Pull Request Label | Section in Release Notes     |
| ------------------ | ---------------------------- |
| `breaking`         | 💥 Breaking Changes          |
| `enhancement`      | 🚀 Features                  |
| `removal`          | 🔥 Removals and Deprecations |
| `bug`              | 🐞 Fixes                     |
| `performance`      | 🐎 Performance               |
| `testing`          | 🚨 Testing                   |
| `ci`               | 👷 Continuous Integration    |
| `documentation`    | 📚 Documentation             |
| `refactoring`      | 🔨 Refactoring               |
| `style`            | 💄 Style                     |
| `dependencies`     | 📦 Dependencies              |

<!-- table-release-drafter-sections-end -->

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
[github-repo-example]: https://github.com/megthommes/cookiecutter-python-poetry-example
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