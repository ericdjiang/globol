# globol

<div align="center">

[![Build status](https://github.com/ericdjiang/globol/workflows/build/badge.svg?branch=master&event=push)](https://github.com/ericdjiang/globol/actions?query=workflow%3Abuild)

![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/ericdjiang/globol/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/ericdjiang/globol/releases)
[![License](https://img.shields.io/github/license/ericdjiang/globol)](https://github.com/ericdjiang/globol/blob/master/LICENSE)

End-to-end platform for textual data acquisition, analysis, and visualization.

</div>

## Overview

Globol is structured as a monorepo which contains a number of standalone repositories:

### gletl
Python package which supports data scraping, ingestion, and ETL operations for textual data obtained from multiple websites/API's.

### gldb
Our persistence layer leverages both MongoDB and PostgresDB. This package contains the database scaffolding required to connect and populate these databases, as well as the model definitions.

## Development

Every sub-repo within this monorepo contains its own development guide. Please use a separate terminal (and thus virtualenv) for each Python package in development to ensure that the dependencies are not polluted.

## Docker

Docker is used to simplify the database installation and management. To start up Mongo and Postgres, run:

```
docker-compose up -d
```

This will create two containers named mongodb and pgdb, populated with user credentials and data.

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/ericdjiang/globol/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/ericdjiang/globol/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/ericdjiang/globol)](https://github.com/ericdjiang/globol/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/ericdjiang/globol/blob/master/LICENSE) for more details.
