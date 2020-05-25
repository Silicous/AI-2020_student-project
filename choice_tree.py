from data import tree_format


def uniq_count(rows):
    # count uniq labels(names)
    count = {}
    for row in rows:
        lbl = row[-1]
        if lbl not in count:
            count[lbl] = 0
        count[lbl] += 1
    return count


# didn't used
def isnumer(val):
    return isinstance(val, int) or isinstance(val, float)


class Question():

    def __init__(self, col, value):
        self.col = col  # column
        self.value = value  # value of column

    def compare(self, example):
        # compare val in example with val in the question
        val = example[self.col]
        if isnumer(val):  # in case menu have prices
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # just to print
        condition = "=="
        if isnumer(self.value):
            condition = ">="
        return "Is %s %s %s?" % (tree_format[self.col], condition, str(self.value))


def split(rows, quest):
    # split data into True and False
    t_rows, f_rows = [], []
    for row in rows:
        if quest.compare(row):
            t_rows.append(row)
        else:
            f_rows.append(row)
    return t_rows, f_rows


def gini(rows):
    counts = uniq_count(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity


def info_gain(l, r, current_gini):
    p = float(len(l)) / (len(l) + len(r))  # something like an enthropy
    return current_gini - p * gini(l) - (1 - p) * gini(r)


def find_best_q(rows):
    # best question to split the data
    best_gain = 0
    best_quest = None
    current_gini = gini(rows)
    n_feat = len(rows[0]) - 1

    for col in range(n_feat):
        vals = set([row[col] for row in rows])

        for val in vals:
            quest = Question(col, val)

            t_rows, f_rows = split(rows, quest)

            if len(t_rows) == 0 or len(f_rows) == 0:
                continue

            gain = info_gain(t_rows, f_rows, current_gini)

            if gain >= best_gain:
                best_gain, best_quest = gain, quest

    return best_gain, best_quest


class Leaf:
    # contain a number of how many times the label has appeared in dataset
    def __init__(self, rows):
        self.predicts = uniq_count(rows)


class Decision_Node():
    # contain the question and child nodes
    def __init__(self, quest, t_branch, f_branch):
        self.quest = quest
        self.t_branch = t_branch
        self.f_branch = f_branch


def build_tree(rows):
    # use info gain and question
    gain, quest = find_best_q(rows)

    # no gain = no more question, so return a Leaf
    if gain == 0:
        return Leaf(rows)

    # split into true and false branch
    t_rows, f_rows = split(rows, quest)

    # print out branches
    t_branch = build_tree(t_rows)
    f_branch = build_tree(f_rows)

    # return the child/leaf
    return Decision_Node(quest, t_branch, f_branch)


def print_tree(node, spc=""):
    # if node is a leaf
    if isinstance(node, Leaf):
        print("    " + "Predict", node.predicts)
        return  # end of function

    # Or question
    print("" + str(node.quest))
    # True branch
    print("" + '--> True:')
    print_tree(node.t_branch, spc + "  ")
    # False branch
    print("" + '--> False:')
    print_tree(node.f_branch, spc + "  ")


def classify(row, node):
    # return our prediction in case the node is a leaf
    if isinstance(node, Leaf):
        return node.predicts
    # otherwise go to the child
    if node.quest.compare(row):
        return classify(row, node.t_branch)
    else:
        return classify(row, node.f_branch)


def print_leaf(counts):
    # count prediction
    total = sum(counts.values()) * 1.0
    probs = {}  # probability
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs