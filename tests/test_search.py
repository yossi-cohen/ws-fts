#!env/bin/python

import sys
sys.path.append('.')

from es_rest import ES_rest


def main():
    es_rest = ES_rest()

    # uri_index = 'http://localhost:9200/test/docs/'
    # es_rest.index(uri_index, {"content": "The quick brown fox"})

    uri_search = 'http://localhost:9200/test/docs/_search'
    res = es_rest.search(uri_search, 'fox')
    format_results(res)


def format_results(res):
    """Print results nicely:
    doc_id) content
    """

    if ('error' in res):
        print('ERROR: {}'.format(res['error']['reason']))
        return

    print("%d documents found:" % res['hits']['total'])
    data = [doc for doc in res['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))


if __name__ == '__main__':
    main()
