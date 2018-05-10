SougouCS-Extractor
===================

Introduction
------------

The project uses the *SougouCS* as source of documents for
several purposes: as training data and as source of data to be
annotated.

SougouCS are available from [SougouCS database
download](http://www.sogou.com/labs/resource/list_news.php).

The SougouCS extractor tool generates plain text from a SougouCS
database.

Description
-----------

[extractor.py](extractor.py)
is a Python script that extracts and cleans text from a [SougouCS
database](http://www.sogou.com/labs/resource/list_news.php). 

Usage:

     extractor.py [options]

Options:

     -i,         : input file dir
     -o,         : out file dir
     --help      : display this help and exit
