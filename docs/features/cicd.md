# CI/CD with Github actions

A `.github` directory is
added with the following structure:

    .github
    ├── actions
    │    └── setup-poetry-env
    │         └── action.yml
    ├── workflows
    │    ├── labeler.yml
    │    ├── pull-request.yml
    │    └── release.yml
    ├── dependabot.yml
    ├── labels.yml
    └── release-drafter.yml

## Actions

`setup-poetry-env` sets up the poetry environment for workflows.

## Workflows

`labeler` sets labels as specified in `labels.yml`. This is required for releasing a new version of the project.

`pull-request` runs quality checks and tests on pull requests.

`release` creates a new release for the project with release notes, publishing to PyPI / Artifactory and generating docs if specified. To learn more about these features, see [Publishing to PyPI or Artifactory](./publishing.md) and [Documentation with MkDocs](./mkdocs.md)

Additionally, all workflows check for compatibility with multiple Python
versions.

# How to trigger a release?

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