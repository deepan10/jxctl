************************
Commands Help References
************************

jxctl
=====

.. code:: bash
    
    Usage: jxctl [OPTIONS] COMMAND [ARGS]...

    Jenkins cli interface for Jenkins Instance

    Options:
    --help  Show this message and exit.

    Commands:
    context  Set and Get Jenkins context
    get      List the Resources(jobs, plugin, build, nodes, etc..
    job      Job level Operations
    version  Show the version and info of jxctl

jxctl get
=========

.. code:: bash

    Usage: jxctl get [OPTIONS] COMMAND [ARGS]...

    List the Resources(jobs, plugin, build, nodes, etc.. ) from Jenkins
    context

    Options:
    --help  Show this message and exit.

    Commands:
    jobs     List Jenkins Context jobs
    plugins  List all installed plugins of Jenkins Context

jxctl get jobs
==============

.. code:: bash

    Usage: jxctl get jobs [OPTIONS]

    List Jenkins Context jobs

    Options:
    -c, --count     Returns number of jobs
    --all           List all(maven, freestly, pipeline,
                    multi-branch, matrix and org) jobs
    --maven         List all maven style jobs
    --freestyle     List all freestyle jobs
    --pipeline      List all pipeline jobs
    --multi-branch  List all multi-branch pipeline jobs
    --matrix        List all matrix jobs
    --folders       List all folders in Jenkins context
    --org           List all Organization jobs
    --help          Print help message

jxctl get plugins
=================

.. code:: bash

    Usage: jxctl get plugins [OPTIONS]

    List all installed plugins of Jenkins Context

    Options:
    -c, --count  Returns the number of plugin installed
    --help       Show this message and exit.

jxctl job
=========

.. code:: bash

    Usage: jxctl job [OPTIONS] JOBNAME

    Job level Operations

    Options:
    --debug              Returns complete job info
    --build              Triggers the build
    --report             Generate HTML report
    --buildinfo INTEGER
    --help               Show this message and exit.
