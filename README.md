human_dates
===========

I came from the Ruby/Rails world and I missed some of my date sugar.  And I found that I kept on resolving this problem
So sharing it.

Note I stole much of this from the following StackOverflow post: http://stackoverflow.com/a/1551394/192791


Installation
------------

.. code-block:: bash

    $ pip install human_dates


Usage
-----

.. code-block:: python

    from human_dates import time_ago_in_words, begining_of_day

    print time_ago_in_words()
    #prints "just now"

    print time_ago_in_words(begining_of_day())
    # prints 8 hours ago
