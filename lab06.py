from scipy.spatial.distance import cosine
import math

fs = open("C:\\PZ\\glove.6B.100d.txt", 'r', encoding="utf8")

def TOEFLParser(filename):
    tF = open(filename, 'r')
    state = 0
    question_words = []
    posiibilities_bag = []
    for line in tF:
        if len(line.split()) == 0:
            question_words.append(question_word)
            posiibilities_bag.append(possibilities)
            state = 0
        elif len(line.split()) == 2:
            if state == 0:
                question_word = line.split()[1]
                possibilities = []
                state = 1
            # if state == 1:
            #     possibilities.append(line.split()[1])
        else:
            if line.split()[3] ==

def cosine2(v1, v2):
    v1v2 = 0
    for i in  range(100):
        v1v2 += v1[i] * v2[i]
    v1norm = 0
    for i in range(100):
        v1norm += v1[i] * v1[i]
    v1norm = math.sqrt(v1norm)
    v2norm = 0
    for i in range(100):
        v2norm += v2[i] * v2[i]
    v2norm = math.sqrt(v2norm)
    return v1v2/(v1norm*v2norm)

# glove pennington

model = {}

for i, line in enumerate(fs):
    if(i%10000 == 0):
        print(i)
    tokens = line.split()
    vec = [0 for i in range(100)]
    for i in range(100):
        vec[i] = float(tokens[i+1])
    model[tokens[0]] = vec

# king_vec = model["king"]
# queen_vec = model["queen"]
# man_vec = model["man"]
# woman_vec = model["woman"]
#
# print(king_vec)
#
# print(cosine(king_vec, queen_vec))
# print(cosine(king_vec, man_vec))
# print(cosine(queen_vec, woman_vec))
# print(cosine(king_vec, woman_vec))
#
# print(cosine2(king_vec, queen_vec))
# print(cosine2(king_vec, man_vec))
# print(cosine2(queen_vec, woman_vec))
# print(cosine2(king_vec, woman_vec))

(question_words, possibilities_bag, answers) = TOEFLParser("C:\\PZ\\toefl.txt")
print(question_words)
print(possibilities_bag)
print(len(answers))

true_positives = 0
for i in range(80):
    maxSimilarity = -1
    try:
        sim1 = cosine2(model[question_words[i]], model[possibilities_bag[i][0]])
        sim2 = cosine2(model[question_words[i]], model[possibilities_bag[i][1]])
        sim3 = cosine2(model[question_words[i]], model[possibilities_bag[i][2]])
        sim4 = cosine2(model[question_words[i]], model[possibilities_bag[i][3]])
    except:
        sim1 = 0.5
        sim2 = 0.5
        sim3 = 0.5
        sim4 = 0.5

    if sim1 > maxSimilarity:
        maxSimilarity = sim1
        answer = 0
    if sim2 > maxSimilarity:
        maxSimilarity = sim2
        answer = 1
    if sim3 > maxSimilarity:
        maxSimilarity = sim3
        answer = 2
    if sim4 > maxSimilarity:
        maxSimilarity = sim4
        answer = 3
    if answer == answers[i]:
        print('ok')
        true_positives += 1

print(true_positives/80.0)