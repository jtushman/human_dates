human_dates
===========

I came from the Ruby/Rails world and I missed some of my date sugar.  And instead of keeping complaining about it, I
thought I would do something about it


It offers two sets of functionality:

#. and foremost it has a nice `time_ago_in_words` function.
#. has some natural language for getting to the beginning and end of things

Note I stole much of this from the following StackOverflow post: http://stackoverflow.com/a/1551394/192791

Note: when you do not pass a time into a function it uses `datetime.utcnow()`


Installation
------------

.. code-block:: bash

    $ pip install human_dates


time_ago_in_words Usage
-----

.. code-block:: python

    from human_dates import time_ago_in_words, beginning_of_day

    print time_ago_in_words()
    #prints "just now"

    print time_ago_in_words(beginning_of_day())
    # prints 8 hours ago


Natural Language Helpers

.. code-block:: python

    from human_dates import *

    print beginning_of_day()
    print beginning_of_hour()
    print beginning_of_year()
    print end_of_month()
    # and so on ....

    # you can also pass a datetime to each of these functions
    import human_dates
    from datetime import datetime
    date = datetime.strptime('Feb 13 2008  1:33PM', '%b %d %Y %I:%M%p')
    result = human_dates.end_of_month(date)
    print result
    # 2008-02-29 23:59:59.999999


Alternatives
------------

- Delorean: http://delorean.readthedocs.org/en/latest/quickstart.html  (<-- please look at this before using human_dates.
It's heavyweight for me but might be great for you)

Other Important Time Libraries
- DateUtil: http://labix.org/python-dateutil
- PyTz: http://pytz.sourceforge.net/


