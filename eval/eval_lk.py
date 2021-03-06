
MODEL_FILE = '../my_data/model.predict.txt'
LABEL_FILE = '../data/lk_test.txt'

def match(k1, ks):
    for k2 in ks:
        if k1 in k2 or k2 in k1: return True
    return False

author2words = {}
for line in open(MODEL_FILE):
    inputs = line.strip().split(',')
    author = inputs[0]
    author2words[author] = []
    for keyword in inputs[1: ]:
        author2words[author].append(keyword)

rt, rt_cnt = 0.0, 0
for i, line in enumerate(open(LABEL_FILE)):
    inputs = line.strip().split(',')
    author = inputs[0]
    keywords = set(inputs[1 :])

    pos_cnt, neg_cnt = 0, 0

    for keyword in author2words[author][: 5]:
        if match(keyword, keywords):
            pos_cnt += 1
        else:
            neg_cnt += 1
    rt += 1.0 * pos_cnt / (pos_cnt + neg_cnt)
    rt_cnt += 1
print rt / rt_cnt, rt_cnt