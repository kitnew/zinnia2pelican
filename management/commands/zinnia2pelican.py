from __future__ import unicode_literals

import errno
import logging
import os

from django.core.management.base import BaseCommand, CommandError

from zinnia.models import Entry
from zinnia.settings import MARKUP_LANGUAGE

class Command(BaseCommand):
    args = '[output_dir]'
    help = 'Export Blog Entries(Markdown only), default directory is "output"'

    def handle(self, *args, **options):

        if MARKUP_LANGUAGE != 'markdown':
            self.stdout.write('The MARKUP_LANGUAGE of blog is not Markdown.\n')
            return

        # make output dir
        output_dir = os.path.join(os.getcwd(), 'output')

        if (len(args) > 0):
            output_dir = args[0]

        try:
            os.makedirs(output_dir)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(output_dir):
                pass
            else:
                logging.exception('')
                raise CommandError('Failed to create directory!')

        if not os.path.isabs(output_dir):
            output_dir = os.path.join(os.getcwd(), output_dir)
        self.stdout.write("Exporting to: '%s' ...\n" % output_dir)

        # No need to export the Author field, pelican provides a default value.
        #Author: %s

        template = '''\
Title: %s
Date: %s
Modified: %s
%sTags: %s
Slug: %s
Summary: %s

%s
'''

        # export each blog entry
        for entry in Entry.objects.all():
            # full path of output file
            filename = entry.slug + '.md'
            output_path = os.path.join(output_dir, filename)

            # make category meta data
            category = ''
            for c in entry.categories.all():
                category += ',' + c.title

            if entry.categories.count() > 0:
                category = '\nCategory: ' + category + '\n'

            # write to file
            f = file(output_path, 'w')
            f.write(template % (
                entry.title,
                entry.creation_date,
                entry.last_update,
                category,
                entry.tags,
                entry.slug,
                #(entry.authors.all())[0],
                entry.excerpt,
                entry.content))
            f.close()

        self.stdout.write('%d file(s) exported.\n' % Entry.objects.count())
        self.stdout.write('Done!\n')

