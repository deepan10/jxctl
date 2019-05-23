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

Add new context
---------------

.. code:: bash

    jxctl context set <CONTEXT_NAME> --url <Jenkins URL> --user <Username> --token <Password/Access Token>
    jxctl context set <CONTEXT_NAME> --url <Jenkins URL> --user <Username> --token <Password/Access Token> --default

Context Info
------------

.. code:: bash

    jxctl context info

List context
------------

.. code:: bash

    jxctl context list
    jxctl context list --all

Update context
--------------

.. code:: bash

    jxctl context set <CONTEXT_NAME> --url <Jenkins URL>
    jxctl context set <CONTEXT_NAME> --user <Username> --token <Password/Access Token>

Rename context
--------------

.. code:: bash

    jxctl context rename <CONTEXT_FROM> <CONTEXT_TO>

Delete context
--------------

.. code:: bash

    jxctl context delete <CONTEXT_NAME>

Usage
=====

Version
-------

.. code:: bash

    jxctl version

Jobs List
---------

.. code:: bash

    jxctl get jobs --all -f table
    jxctl get jobs --maven --freestyle --count -f json
    jxctl get jobs --pipeline -c
    jxctl get jobs --folders -f json

Folders List
------------

.. code:: bash

    jxctl get folders -f table
    jxctl get folders -c

Plugins List
------------

.. code:: bash

    jxctl get pluings
    jxctl get pluings -c

Nodes List
----------

.. code:: bash

    jxctl get nodes
    jxctl get nodes -c -f table

Job
---

Job info
________

.. code:: bash

    jxctl job <JOB NAME>
    jxctl job <JOB NAME> --format table

Delete a job
____________

.. code:: bash
    
    jxctl job <JOB NAME> --delete

Trigger job build
_________________

.. code:: bash

    jxctl job <JOB NAME> --build
    jxctl job <JOB NAME> --build --params <JSON>

Build info
__________

.. code:: bash
    
    jxctl job <JOB NAME> --buildinfo <Build Number>

Abort a build
_____________

.. code:: bash
    
    jxctl job <JOB NAME> --abort <Build Number>

Plugin
------

.. code:: bash

    jxctl plugin <Plugin Name>

Node
----

Node info
_________

.. code:: bash

    jxctl node <NODE NAME>
    jxctl node <NODE NAME> -f table

Make offline
____________

.. code:: bash

    jxctl node <NODE NAME> --make-offline
    jxctl node <NODE NAME> --make-offline -m <MESSAGE>

Make online
___________

.. code:: bash

    jxctl node <NODE NAME> --make-online