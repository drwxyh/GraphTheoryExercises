from collections import namedtuple


if __name__ == "__main__":
    Snake = namedtuple('Snake', ['f', 't']) # type: __main__.Snake
    Lift = namedtuple('Lift', ['f', 't']) # type: __main__.Lift
    with open('2.9') as fp:
        n, s, l = [int(x) for x in fp.readline().strip('\n').split(' ')]
        N = n * n
        graph = ['O' for i in range(0, N)]

        snake_data = [int(x) for x in fp.readline().strip('\n').split(' ')]
        snake_list = list()
        for i in range(0, s):
            graph[snake_data[2 * i] - 1] = Snake(snake_data[2 * i] - 1, snake_data[2 * i + 1] - 1)

        lift_data = [int(x) for x in fp.readline().strip('\n').split(' ')]
        lift_list = list()
        for i in range(0, l):
            graph[lift_data[2 * i] - 1] = Lift(lift_data[2 * i] - 1, lift_data[2 * i + 1] - 1)

        graph[0] = 'V'
        step = 0
        while graph[N-1] != 'V':
            step += 1
            search_list = list()
            for i in range(0, N):
                if graph[i] == 'V':
                    search_list.append(i)

            for x in search_list:
                for j in range(1, 7):
                    u = x + j
                    if u in range(0, N):
                        if graph[u] == 'O' or graph[u] == 'V':
                            graph[u] = 'V'
                        else:
                            graph[graph[u].t] = 'V'

        print(step)