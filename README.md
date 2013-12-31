zinnia2pelican
==============

Exports [Zinnia](http://django-blog-zinnia.com/) blog entries in the formats of [Pelican](http://getpelican.com/), by adding a simple hook into Django's ``manage.py``.

Markdown is the only currently supported format.

Tested for Zinnia version 0.9-dev.

## Install

Download the [source package](https://github.com/kitnew/zinnia2pelican/archive/master.zip), unzip it and drop in your Django project directory. It may looks like:

    /path/to/your/django/project/zinnia2pelican

Then add the app into ``INSTALLED_APPS`` within Django's project ``settings.py``:

    INSTALLED_APPS = (
        ...
        'zinnia2pelican',
    )


## Usage

Change the path to your Django project:

    $ cd /path/to/your/django/project/

Then run the command:

    $ python manage.py zinnia2pelican ~/your_blog


    Export to: '/Users/your_name/your_blog' ...
    11 file(s) exported.
    Done!


## Uninstall

Just delete the `zinnia2pelican` directory, and comment out the item which added into ``INSTALLED_APPS`` within Django's project ``settings.py``.


## Credits

* Mo Nianliang ([KitNew Blog](http://kitnew.com/))


## License

Released under MIT license.

