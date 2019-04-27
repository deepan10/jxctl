# Welcome to Jxctl

A command line interface for Jenkins.

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
