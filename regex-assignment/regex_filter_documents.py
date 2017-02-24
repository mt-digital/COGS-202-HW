'''
Regular Expression Assignment COGS 202.

Given a regular expression and a directory with documents, create a new
directory with documents that contain a matching expression.

Author: Matthew Turner
Date: February 16, 2017

To run:
    python regex_filter_documents.py <regex> <input_document_dir> <filtered_doc_dir>

Try the following example using the sample_inputs/ directory included in
the repository. Make sure to put quotes around the regex or bash might think
you're doing glob expansion.

Examples:
    python regex_filter_documents.py ".*[A-Z]{2,}.*" sample_inputs two_or_more_caps
    python regex_filter_documents.py ".*\d{2,}.*" sample_inputs two_or_more_numbers
    python regex_filter_documents.py "^M.*" sample_inputs starts_with_M
'''
import os
import re
import shutil


def filter_docs(regex, input_dir, output_dir, clobber=True):
    '''
    Create new directory `output_dir` that will contain all documents from
    `input_dir` that match the regex. It is not recursive, so will only
    check files in `input_dir`, not files in subdirectories of `input_dir`.

    Arguments:
        regex (str): regular expression used to filter files
        input_dir (str): directory to look for input files
        output_dir (str): directory to place output files; overwritten if
            clobber is True
        clobber (bool): whether or not to overwrite output_dir; error if
            output_dir exists and clobber=True
    '''

    # prepare output directory
    if os.path.isdir(output_dir):

        if not clobber:
            raise RuntimeError('clobber is false and output_dir exists')

        shutil.rmtree(output_dir)

    os.mkdir(output_dir)

    # filter and copy if file matches the filter
    compiled_regex = re.compile(regex)

    for f in os.listdir(input_dir):

        try:
            text = open(os.path.join(input_dir, f), 'r').read()

            if compiled_regex.match(text):
                outfile = os.path.join(output_dir, os.path.basename(f))
                open(outfile, 'w').write(text)

        except:
            print('Encountered error with file {}, skipping...'.format(f))


USAGE = '''
python regex_filter_documents.py <regex> <input_document_dir> <filtered_document_dir>
'''

if __name__ == '__main__':

    import sys

    try:
        regex = sys.argv[1]
        input_document_dir = sys.argv[2]
        filtered_document_dir = sys.argv[3]
    except:
        print(USAGE)

    filter_docs(regex, input_document_dir, filtered_document_dir)
