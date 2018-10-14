#!env/bin/python

import sys
sys.path.append('.')

from es_rest import ES_rest


def main():
    es_rest = ES_rest()

    # uri_index = 'http://localhost:9200/test/docs/'
    # es_rest.index(uri_index, {"content": "The quick brown fox"})

    uri_search = 'http://localhost:9200/test/docs/_search'
    results = es_rest.search(uri_search, 'fox')
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
