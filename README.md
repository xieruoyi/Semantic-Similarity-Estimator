# Semantic-Similarity-Estimator
In this project, an intelligent system is built to estimate the semantic similarity of any given pair of words. In this way, the system can quickly find the synonym of a word, provided a group of candidates.

The semantic similarity is measured using the semantic descriptor vector of each word, which is represented as  where  is the number of sentences in which both the word  and  have appeared. For example, in the paragraph

I am a sick man. I am a spiteful man. I am an unattractive man.
​ -- From Notes from the Underground by Fyodor Dostoyevsky
descriptor = {'i':3,'am':3,'a':2,'sick':1,'spiteful':1,'an':1,'unattractive':1}

The semantic descriptor vector of each word can be therefore expressed in a similar way, which are vectors u={u1,u2...un} and v = {v1,v2,...,vn}.
Thus, the semantic similarity of the words, u and v, can be calculated as
$$\left( \sum_{i=1}^n u_i v_i \right)\div\left(\sum_{k=1}^n u_i^2 \right) \left( \sum_{k=1}^n v_i^2 \right)^(0.5)$$

 

where ui·vi is the product of the number of times that the given word appears together with the word ui and that it apears together with the word . In other words, if a word only appears with u, but not v, the product of ui·vi will equal 0.

After comparing with all candidates, the word with the highest similarity will be chosen as the synonym.

Usage
Directory Structure
sw.txt, wp.txt and test.txt: all text files that are used to retrieve the synonym of a given word.
synonyms.py: contains all functions to clean up the texts and calculate the semantic similarity.
Testing Example
The functionality can be tested using codes similar to the following:
      sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
      res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
      print(res, "of the guesses were correct")
