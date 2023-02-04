'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math

global semantic_descriptors

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    value = []
    answer = 0
    v1 = 0
    v2 = 0
    top = 0
    for key1, value1 in vec1.items():
        v1 += value1**2
        for key2, value2 in vec2.items():
            if key1 == key2:
                value.append([value1,value2])

    for key2,value2 in vec2.items():
        v2 += value2**2

    for i in range(0,len(value)):
            top += value[i][0]*value[i][1]

    answer = top / ((v1*v2)**0.5)
    return(answer)

def build_semantic_descriptors(sentences):
    d = {}
    for i in range(0,len(sentences)):
        for j in range(0,len(sentences[i])):
            word = sentences[i][j]
            if word not in d:
                d[word] = {} # i
            for k in range(0,len(sentences[i])):
                if sentences[i][k] != word:
                    if sentences[i][k] not in d[word]:
                        d[word][sentences[i][k]] = 0
                        d[word][sentences[i][k]] +=1

                    else:
                        d[word][sentences[i][k]] +=1
    return(d)



def build_semantic_descriptors_from_files(filenames):
    list_1 = []
    num = 0
    lines = []
    for i in range(0,len(filenames)):
        f = open(filenames[i], "r", encoding="latin1")
        text = f.read()
        line = text.lower().replace(","," ").replace("-"," ").replace("--"," ").replace(":"," ").replace(";"," ").replace("!",".").replace("?",".").split(".")


        for j in range(0,len(line)):
            for i in range(0,len(line[j])):
                if line[j][i]!= " " :
                    num += 1
                    if i ==len(line[j])-1:
                        lines.append(line[j][i-num+1:i+1])
                        num = 0
                elif line[j][i] == " " and num != 0:
                    lines.append(line[j][i-num:i])
                    num = 0
            list_1.append(lines)
            lines = []

    return(build_semantic_descriptors(list_1))

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    a = {}
    b = {}
    res = -2
    c = 0
    Choice = ""
    value = []
    for key in semantic_descriptors:
        if key == word:
            a = semantic_descriptors[word]
    for key in semantic_descriptors:
        for i in range(0,len(choices)):
            if key == choices[i]:
                b = semantic_descriptors[choices[i]]
                for key1, value1 in a.items():
                    for key2, value2 in b.items():
                        if key1 == key2:
                            value.append([value1,value2])
                if value == []:
                    c = res
                    res = max(-1,res)
                    if res == -1 and res != c:
                        Choice = choices[i]
                else:
                    c = res
                    res = max(similarity_fn(a,b),res)
                    if res == similarity_fn(a,b) and res != c:
                        Choice = choices[i]
    return(Choice)


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, "r", encoding="latin1")
    text = f.read().split("\n")
    similar_answer = ""
    num = 0
    word = ""
    answer = ""
    choices = ""
    number_of_lines = 0
    for lines in text:
        number_of_lines += 1
        list = lines.split()
        word = list[0]
        answer = list[1]
        choices = list[2:]
        similar_answer = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if similar_answer == answer:
            num += 1
    res = num/number_of_lines*100
    return(res)


if __name__ == '__main__':
#     cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6})
#     print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# # "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
    # print(build_semantic_descriptors_from_files(["mydata.txt","haha.txt"]))
    # # print(cosine_similarity({'I': 3, 'am': 3, 'a': 2, 'sick': 1, 'spiteful': 1, 'an': 1, 'unattractive': 1},{'I': 2, 'am': 2, 'sick': 1, 'man': 2, 'spiteful': 1}))
    # semantic_descriptors =build_semantic_descriptors_from_files(["mydata.txt","haha.txt"])
    # print(semantic_descriptors)
    # print(most_similar_word("disease", ["do","liver","man"], semantic_descriptors, cosine_similarity))
    sem_desc = {"dog": {"cat": 1, "food": 1},"cat": {"dog": 1}}
    print(most_similar_word("dog", ["cat", "rat"], sem_desc,cosine_similarity))
    sem_descriptors = build_semantic_descriptors_from_files(["1.txt", "2.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")