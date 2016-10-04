# TODO: Improve Data Quality
# Enable fuzzy search (McDonald => McDonald's)

This project discovers association rules among California businesses. It can discover relationship such as Taco Bell is always in close affinity with KFC, Apple store is always near the Microsoft stores.

The idea is to group business in close affinity as baskets and use the association rule learning algorithms.


Reference:
https://en.wikipedia.org/wiki/Association_rule_learning

Steps:
1) Please add your own Google API key to credentials.txt: https://console.developers.google.com/iam-admin/iam/project
2) Customize locations.csv to some Latitude, Longitude as the center.
3) Run nearbyRetriever.py, the baskets will be written to baskets.csv. You might need multiple runs to retrieve all the locations.
4) Run analysis.py, this will dump the neighbors relation into neighbors.p
5) Run retrieve.py and query restaurants

e.g.
python retriever.py
Query: KFC
Atticus Creamery + Pies
Fiddler's Bistro
Top Class Pizza
Rubio's
Sato Sushi
