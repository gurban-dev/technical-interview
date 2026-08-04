from collections import defaultdict

# This was the solution to the third problem asked during
# the assessment given by Hudson River Trading.

# This problem is similar to:
# https://leetcode.com/problems/number-of-atoms

def solution(reaction):
    # Parse one side of the reaction.
    def parse_side(side):
        total_counts = defaultdict(int)

        for molecule in side.split("+"):
            molecule = molecule.strip()

            molecule_counts = parse_molecule(molecule)

            for element, count in molecule_counts.items():
                total_counts[element] += count

        return dict(total_counts)

    # Parse a single molecule.
    def parse_molecule(formula):
        i = 0
        n = len(formula)

        # Read optional molecule multiplier.
        molecule_multiplier = 0

        while i < n and formula[i].isdigit():
            molecule_multiplier = molecule_multiplier * 10 + int(formula[i])
            i += 1

        if molecule_multiplier == 0:
            molecule_multiplier = 1

        stack = [defaultdict(int)]

        while i < n:
            if formula[i].isspace():
                i += 1
                continue

            # Start group.
            if formula[i] == "(":
                stack.append(defaultdict(int))
                i += 1

            # End group.
            elif formula[i] == ")":
                group = stack.pop()
                i += 1

                multiplier = 0

                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1

                if multiplier == 0:
                    multiplier = 1

                for element, count in group.items():
                    stack[-1][element] += count * multiplier

            # Parse element.
            else:
                element = formula[i]
                i += 1

                while i < n and formula[i].islower():
                    element += formula[i]
                    i += 1

                count = 0

                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1

                if count == 0:
                    count = 1

                stack[-1][element] += count

        # Apply molecule multiplier.
        result = {}

        for element, count in stack[-1].items():
            result[element] = count * molecule_multiplier

        return result

    left, right = reaction.split("=")

    left_counts = parse_side(left)
    right_counts = parse_side(right)

    return left_counts == right_counts

print("solution(\"2H2 + O2 = 2H2O\"):", solution("2H2 + O2 = 2H2O"))