# `jxctl` 
![CircleCI (all branches)](https://img.shields.io/circleci/project/github/deepan10/jxctl.svg?style=plastic)  ![GitHub](https://img.shields.io/github/license/deepan10/jxctl.svg?style=plastic)

[![codecov](https://codecov.io/gh/deepan10/jxctl/branch/master/graph/badge.svg)](https://codecov.io/gh/deepan10/jxctl)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=jxctl&metric=coverage)](https://sonarcloud.io/dashboard?id=jxctl)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=jxctl&metric=alert_status)](https://sonarcloud.io/dashboard?id=jxctl)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=jxctl&metric=bugs)](https://sonarcloud.io/dashboard?id=jxctl)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=jxctl&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=jxctl)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=jxctl&metric=ncloc)](https://sonarcloud.io/dashboard?id=jxctl)

![PyPI](https://img.shields.io/pypi/v/jxctl.svg?color=f&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jxctl.svg?color=f&style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jxctl.svg?color=f&style=plastic)

![Libraries.io dependency status for specific release](https://img.shields.io/librariesio/release/pypi/jxctl/0.0.6.svg?style=plastic)

[![Documentation Status](https://readthedocs.org/projects/jxctl/badge/?version=latest)](https://jxctl.readthedocs.io/en/latest/?badge=latest)

A Command line interface for Jenkins.

## Installation

    `pip install jxctl`

## Commands

| Command | Description                                         | Usage                    |
|---------|-----------------------------------------------------|--------------------------|
| version | Version and info about `jxctl`                      | `jxctl version`          |
| context | Jenkins instance called as a `context` in `jxctl`. It provides set Jenkins context and infomation about the context | `jxctl context [OPTIONS] COMMAND [ARGS]...` |
| get | `get` provides you the functionality to get the resources like *jobs*, *pluings*, *folders*, *builds* list with *count* | `jxctl get [OPTIONS] COMMAND [ARGS]...`|
| job | `job` provides the functionalities like `create, trigger build, job info, build info` | `jxctl job [OPTIONS] COMMAND [ARGS]`

### context
    Examples:
    `jxctl context set --url <Jenkins URL>`
    `jxctl context set --url <Jenkins URL> --name <Context Name> --user <Username> --token <Password/Access Token>`
    `jxctl context info`
### get
    Examples:
    `jxctl get jobs --all`
    `jxctl get jobs --maven --freestyle --count`
    `jxctl get pluings`

### job
    Examples:
    `jxctl job <JOB NAME>`
    `jxctl job <JOB NAME> --build`
    `jxctl job <JOB NAME> --buildinfo <BUILD NUMBER>`

## Current Work
| Work      |   Description     | Status |
|-----------|-------------------|--------|
| Job       | Implemention Job & Build functionality(Create, Trigger, Detail, Delete) | InProgress | 
| Testing   | Implement Test Cases, Suite | InProgress |
| Handling Error   | Implement Exception Handling | InProgress | 
| Node  | Implement Node functionality | ToDo | 
| Report | Implement Report functionality | ToDo |
| Docs | Document Generation | ToDo |

## Contribution 
We are happy to accept PR's. Those who are interested in contribution please have a look at below functional area's which are needed.

    * Testing
    * Docs
    * Fine-Tuning