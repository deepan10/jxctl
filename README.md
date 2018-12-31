# jxctl [![Build Status](https://travis-ci.com/deepan10/jxctl.png?branch=develop)](https://travis-ci.com/deepan10/jxctl)
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

## Build & Test 

* Travis Build [https://travis-ci.com/deepan10/jxctl](https://travis-ci.com/deepan10/jxctl)
* SonarCloud [https://sonarcloud.io/dashboard?id=jxctl](https://sonarcloud.io/dashboard?id=jxctl)