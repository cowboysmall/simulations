import sys
import random


def simulation(choice, jump = False):
    doors = [0] * 3
    car   = random.randint(0, 2)

    doors[car]    += 1
    doors[choice] += 1

    reveal = random.choice(list(set(range(3)) - set([choice, car])))
    doors[reveal] = -1

    if jump:
        for i in range(3):
            if i != choice and doors[i] != -1:
                doors[choice] -= 1
                doors[i]      += 1

    return doors[car] == 2


def print_results(counter1, counter2, iterations):
    print()
    print('Monte Hall - %s iterations' % (iterations))
    print()
    print('Correct without jumping: %8d' % (counter1))
    print('             Proportion: %8f' % (counter1 / float(iterations)))
    print()
    print('   Correct with jumping: %8d' % (counter2))
    print('             Proportion: %8f' % (counter2 / float(iterations)))
    print()


def main(argv):
    iterations = int(argv[0])

    random.seed(1337)

    counter1 = 0
    counter2 = 0
    for _ in range(iterations):
        if simulation(random.randint(0, 2)):
            counter1 += 1
        if simulation(random.randint(0, 2), True):
            counter2 += 1

    print_results(counter1, counter2, iterations)


if __name__ == "__main__":
    main(sys.argv[1:])

