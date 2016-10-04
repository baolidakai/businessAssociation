'''
For each business A, stores the counter for other nearby business
Then sort them by Pr(B | A) / Pr(B) = count(A and B) / count(A) / count(B) * total count <=> count(A and B) / (count(A) * count(B)) <=> count(A and B) / count(B)
'''
from collections import defaultdict
import pickle

neighbors = defaultdict(dict)
retriever = dict()

with open('baskets.csv', 'r') as f:
  for line in f:
    basket = line.split(',')[2:]
    if not basket:
      continue
    for i in range(len(basket)):
      business1 = basket[i].strip()
      for j in range(i + 1, len(basket)):
        business2 = basket[j].strip()
        if business1 == business2:
          continue
        if business2 not in neighbors[business1]:
          neighbors[business1][business2] = 0
        if business1 not in neighbors[business2]:
          neighbors[business2][business1] = 0
        neighbors[business1][business2] += 1
        neighbors[business2][business1] += 1
  f.close()

for query in neighbors:
  candidates = neighbors[query]
  candidates = sorted(candidates.items(), key = lambda result: result[1] / (sum(neighbors[result[0]].values()) + 1E-6), reverse = True)[:5]
  rtn = '\n'.join(candidate[0] + ' ' + str(candidate[1]) for candidate in candidates)
  retriever[query] = rtn

pickle.dump(neighbors, open('neighbors.p', 'wb'))
pickle.dump(retriever, open('retriever.p', 'wb'))
