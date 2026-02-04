from itertools import combinations

class KnowledgeBase:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        if clause not in self.clauses:
            self.clauses.append(clause)

    def pl_resolution(self, query):
        clauses = self.clauses + [negate_clause(query)]
        new = set()

        while True:
            pairs = combinations(clauses, 2)
            for (ci, cj) in pairs:
                resolvent = resolve(ci, cj)
                if not resolvent:
                    continue
                if resolvent == []:
                    return True
                new.add(tuple(sorted(resolvent)))

            if new.issubset(set(map(tuple, clauses))):
                return False
            clauses += list(map(list, new))


def negate_clause(clause):
    return [[-lit for lit in literals] for literals in clause]


def resolve(c1, c2):
    for lit in c1:
        if -lit in c2:
            temp1 = [x for x in c1 if x != lit]
            temp2 = [x for x in c2 if x != -lit]
            return temp1 + temp2
    return None
