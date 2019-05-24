import random
import math
import afunction
import dekoder

def crossover(parents):
    # print("crossover")

    first_parent = parents[0]
    second_parent = parents[1]
    offspring_size = len(parents[0])
    crossover_point = random.randint(0, offspring_size - 1)
    offspring = ['', '']
    offspring[0] += (first_parent[0:crossover_point])
    offspring[1] += (second_parent[0:crossover_point])
    offspring[1] += (first_parent[crossover_point:offspring_size])
    offspring[0] += (second_parent[crossover_point:offspring_size])

    return offspring


def mutation(offspring):
    # print("mutation")
    nb = 0
    for i in range(len(offspring)):
        rand = random.randint(0, 2 * len(offspring))
        if rand == 0:
            nb += 1
            offspring[i] = str((int(offspring[i]) + 1) % 2)
    return offspring


def get_parents(population):
    # print("get parents")
    first_parent_index = random.randint(0, len(population) - 1)
    second_parent_index = random.randint(0, len(population) - 1)
    while first_parent_index == second_parent_index:
        second_parent_index = random.randint(0, len(population) - 1)
    return [population[first_parent_index], population[second_parent_index]]


def kill(population, mi, d):
    overall = 0
    temp_af = []
    maxx = 0.0
    max_i = 0
    for i in range(len(population)):
        # print("licze overall")

        x = dekoder.decode(population[i])[0]
        y = dekoder.decode(population[i])[1]
        a = dekoder.decode(population[i])[2]
        temp_af.append(math.exp(afunction.J(x, y, a, d)[0]) ** 2)
        overall += temp_af[i]
        if maxx != max(maxx, temp_af[i]):
            maxx = max(maxx, temp_af[i])
            max_i = i

    overall = round(overall, 4)
    survivals = [population[max_i]]

    for _ in range(mi - 1):
        # print("wylosowano osobnika")

        temp = overall
        temp *= 10000
        temp = round(temp)
        rand = random.randint(0, temp - 1)
        rand /= 10000
        for i in range(len(population)):
            if temp_af[i] <= rand:
                rand -= temp_af[i]
            else:
                survivals.append(population[i])
                break
    return survivals


class SJ:

    def __init__(self, d):
        self.d = d

    def simple_J(self, element):
        x = dekoder.decode(element)[0]
        y = dekoder.decode(element)[1]
        a = dekoder.decode(element)[2]
        return afunction.J(x, y, a, self.d)[0]


class SJF:

    def __init__(self, d):
        self.d = d

    def simple_J(self, element):
        x = dekoder.decode(element)[0]
        y = dekoder.decode(element)[1]
        a = dekoder.decode(element)[2]
        return afunction.J_return_forbidden(x, y, a, self.d)


def kill2(population, mi, d):
    sorter = SJ(d)
    population.sort(key=sorter.simple_J, reverse=True)

    return population[:mi]


def best_v(population, d):
    sum = 0
    best_value = 0
    for i in population:
        x = dekoder.decode(i)[0]
        y = dekoder.decode(i)[1]
        a = dekoder.decode(i)[2]
        value = afunction.J(x, y, a, d)[0]
        sum += value
        best_value = max(value, best_value)
        if best_value >= 0.9:
            break

    return best_value, sum/len(population)


def best_positions(population, d):
    best_value = 0
    tab = []

    max_x = dekoder.decode(population[0])[0]
    max_y = dekoder.decode(population[0])[1]
    max_a = dekoder.decode(population[0])[2]
    for i in population:
        dek = dekoder.decode(i)
        x = dek[0]
        temp_x = x[:]
        y = dek[1]
        temp_y = y[:]
        a = dek[2]
        temp_a = a[:]
        J = afunction.J(temp_x, temp_y, temp_a, d)

        maxx = max(J[0], best_value)
        if maxx != best_value:
            best_value = max(maxx, best_value)
            max_x = x
            max_y = y
            max_a = a
            tab = J[1]
    return max_x, max_y, max_a, tab


def first_population(sensors, mi, d):
    population = []
    done = False
    for i in range(mi):
        genes = []
        gene_part = ''
        for _ in range(sensors):
            while True:
                gene_part = ''
                for _ in range((math.ceil(math.log2(dekoder.n())) + math.ceil(math.log2(dekoder.m())) + 2)):
                    rand = random.randint(0, 1)
                    gene_part += str(rand)
                if not done:
                    tp = afunction.j_for_one(dekoder.decode(gene_part)[0][0], dekoder.decode(gene_part)[1][0], d)
                else:
                    tp = [0, 0]
                if not tp[1]:
                    break
            genes.append(gene_part)
        new_gene = ''
        while genes:
            new_gene += genes.pop()
        s = SJ(d)
        power = s.simple_J(new_gene)

        print(i + 1, "/", mi, " genotypes created (power: ", power, ")")
        if power >= 0.9:
            done = True
        population.append(new_gene)
    print("first population created")
    return population


def main_gen(mi, lambdaa, d, sensors):
    same = 0
    best = 0
    population = first_population(sensors, mi, d)
    pop = 0
    while best < 0.9 and same < 100:
        offspring = []
        for _ in range(lambdaa // 2):  # lambda musi byc parzysta!!
            offspring.extend(mutation(crossover(get_parents(population))))
        population.extend(offspring)
        temp_best = best_v(population, d)
        if best >= temp_best[0]:
            same += 1
        else:
            best = temp_best[0]
            same = 0

        pop += 1
        print("max area: ", best)
        print("average area: ", '{:06.4f}'.format(temp_best[1]))
        print("population: ", pop)
        print("to go: ", 100-same)
        print("sensors: ", sensors)
        print()

        if best >= 0.9:
            break

        population = kill2(population, mi, d)

    return best, best_positions(population, d)


def last_gen(mi, lambdaa, d, sensors):
    same = 0
    best = 0
    population = first_population(sensors, mi, d)
    pop = 0
    while best < 0.9:
        offspring = []
        for _ in range(lambdaa // 2):  # lambda musi byc parzysta!!
            offspring.extend(mutation(crossover(get_parents(population))))
        population.extend(offspring)
        temp_best = best_v(population, d)
        if best >= temp_best[0]:
            same += 1
        else:
            best = temp_best[0]
            same = 0

        pop += 1
        print("max area: ", best)
        print("average area: ", '{:06.4f}'.format(temp_best[1]))
        print("population: ", pop)
        print("sensors: ", sensors)
        print()

        if best >= 0.9:
            break

        population = kill2(population, mi, d)

    return best, best_positions(population, d)
