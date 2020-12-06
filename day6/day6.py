def part1():
    with open('day6/input.txt') as f:
        input = f.read()

        groups = input.split('\n\n')
        sums = []
        for group in groups:
            unique_answers = set()
            group = group.split('\n')
            for person in group:
                for answer in person:
                    unique_answers.add(answer)

            sums.append(len(unique_answers))
        print(sums)
        print(sum(sums))

with open('day6/input.txt') as f:
    string = ""
    all = 0
    total = 0
    totalAll = 0
    for line in f.read().split("\n"):
        if line != "":
            string += line
            all += 1
        else:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord("a")] += 1
            for letter in letters:
                total += (letter > 0)
                totalAll += (all == letter)
            string = ""
            all = 0

# part 1
print(total)
# part 2
print(totalAll)
