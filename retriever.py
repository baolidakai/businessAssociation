'''
Retriever to retrieve the most associated neighbors of a business A
Sort neighbors B by count(AB) / count(B)

TODO: Enable fuzzy matching
'''
import pickle

retriever = pickle.load(open('retriever.p', 'rb'))
while True:
  query = input('Query: ')
  if query not in retriever:
    print('Done.')
    break
  print(retriever[query])
