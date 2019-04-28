************
User Guide
************

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents:

Installation
============

Install the package (or add it to your ``requirements.txt`` file):

.. code:: bash

    pip install jxctl

Configuration
=============

.. code:: bash

    jxctl context set --url <Jenkins URL> --name <Context Name> --user <Username> --token <Password/Access Token>
    jxctl context set --url <Jenkins URL>
    jxctl context set --user <Username> --token <Password/Access Token>

.. toctree::
   :maxdepth: 3

Usage
=====

Version
-------

.. code:: bash

    jxctl version

Jobs & Folder list
------------------

.. code:: bash

    jxctl get jobs --all
    jxctl get jobs --maven --freestyle --count
    jxctl get jobs --pipeline -c
    jxctl get jobs --folders

Get Plugins
-----------

.. code:: bash

    jxctl get pluings
    jxctl get pluings -c

Job Details
-----------

.. code:: bash

    jxctl job <JOB NAME>
    jxctl job <JOB NAME> --build
    jxctl job <JOB NAME> --buildinfo <BUILD NUMBER>
