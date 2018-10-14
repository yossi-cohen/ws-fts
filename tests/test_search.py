#!env/bin/python

import sys
sys.path.append('.')

from search import search


def main():
    uri = 'http://localhost:9200/test/docs/_search'
    results = search(uri, 'fox')
    format_results(results)


def format_results(results):
    """Print results nicely:
    doc_id) content
    """

    if ('error' in results):
        print('ERROR: {}'.format(results['error']['reason']))
        return

    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))


if __name__ == '__main__':
    main()
