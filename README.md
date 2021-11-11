# Twitter-Event-Detection

## Questions:
  - Import problem: when importing the sedwik model problem with some imports from sedwik.main. 
  - Summarization: Found some algorithms for LaxRank, yet results are not good. given a set of events - the most similar event to other events is returned.

## Answers: 
  - save a local db. for all received tweets for reuse. 
  - probably two parallel threads - first is a requests listener from front end, second for tweets requests from twitter.
  - sol for Import Problem: move import files into its dir.   
  - sol fro Sum: find summarization for most important words, get most important words with POS (part of speech), language model bert (humming face) - given a word it will tell     the next word (can do fine tuning). *for now i suggest searching for an existing algorithms or models for it (ask Maor, maybe he knows)*
  - did maor implement code that transfers db. format to sedwik format? *I assume he did, but not sure about it*
