# Release 4.3.0

- Remove the ISSUE_TEMPLATE relying on the .github repository for the defaults.
- Add new workflows:
  - py-temp-fork-pvt_merge_with_local-def.yaml
  - py-temp-fork-scheduled_sync_with_upstream-def.yaml
- Removed workflow:
  - python-template-pypi-public-no-docker.yaml
- Updated config files
  - .gitignore
  - pre-commit-config.yaml
- Updated scripts
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 4.2.5

- Updated workflows
  - py-temp-dep-pvt_no_docker-fork.yaml
  - py-temp-fork-sync-def.yaml
- Update configuration files
  - .gitignore
  - .pre-commit-config.yaml
  - pyproject.toml
- Update scripts
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 4.2.5

- Update ISSUE_TEMPLATE's
- Implement GitHub Reusable workflows.
- Remove unnecessary doc folder.
- Upgrade to support Python 13.1
- Update formatting configuration files
  - flake8
  - .gitattributes
  - .gitignore
  - .pre-commit-config.yaml
  - readthedocs.yaml
  - rstcheck.cfg
- Delete redundant files
  - Docker files
  - install.ps1
- Add utility scripts
  - InstallDevEnv.ps1
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 5.2.4

- Increase python range to 3.10 to later
- Upgrade pyproject.toml to Poetry 2.0.1

______________________________________________________________________

# Release 5.2.3

- Update ISSUE_TEMPLATE
  - release.md

______________________________________________________________________

# Release 5.2.2

- Update ISSUE_TEMPLATE
  - bugfix.md
- Update GitHub Workflows
  - Cleanup 04-build-and-publish-to-pypi.yaml

______________________________________________________________________

# Release 5.2.0

- Update ISSUE_TEMPLATE's
- Update GitHub Workflows
- Implemented Poetry

______________________________________________________________________
