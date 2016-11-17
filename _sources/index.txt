.. Laser-Writer documentation master file, created by
   sphinx-quickstart on Wed Nov 16 20:53:26 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Laser-Writer's documentation!
========================================

Introduction
------------

**Description:** A laser writer that uses `mirror galvonometers <https://en.wikipedia.org/wiki/Mirror_galvanometer>`_ to control a laser beam and write tweets on distant objects

Source code available here https://github.com/MalcolmWilliams/Laser-Writer


Helper Modules:
++++++++++++++++
- `Select_Tweet <https://malcolmwilliams.github.io/Laser-Writer/code.html#module-Select_Tweet>`_ selects a tweet from a pool of available tweets based on certain characteristics.

- `Retrieve_Tweets <https://malcolmwilliams.github.io/Laser-Writer/code.html#module-Retrieve_Tweets>`_ uses twitter's API retrieve tweets aimed at the desired source, perform black listing and store the tweet data in a text file.

- `Openlase_Driver <https://malcolmwilliams.github.io/Laser-Writer/code.html#module-Openlase_Driver>`_  provide an abstraction layer on the openlase library. The tweet text is sent here and is then formatted and sent to the laser.


Contents
--------
.. toctree::
    :maxdepth: 2
    
    code.rst


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



