from aproxymation import Aproxymation

def split_data(data, ratio, shuffle = False):
    if shuffle:
        d1 = []
        d2 = []
        if ratio < 1:
            ratio = int(1 / ratio)
        for i in range(0, len(data) // (ratio + 1) * (ratio + 1), ratio + 1):
            for j in range(ratio):
                d1.append(data[i + j])
            d2.append(data[i + ratio])
        if ratio >= 1:
            return d1, d2
        return d2, d1
    return data[:int(ratio * len(data))], data[int((1 - ratio) * len(data)):]

class Model:
    def __init__(self, points, **kwargs):
        self.max_n = kwargs.get('max_n', -1)
        train_mode = kwargs.get('train_mode', 'e')
        data_split_ratio = kwargs.get('data_split_ratio', 1)
        if self.max_n == -1:
            self.max_n = len(points)
        self.points = points

        self.best_n = -1
        self.best_e = -1

        if train_mode == 'e':
            self.w = Aproxymation(points)
            self.train(self.e)
        elif train_mode == 'data':
            train_points, test_points = split_data(points, data_split_ratio, True)
            self.w = Aproxymation(train_points)
            self.train(self.get_data_e_function(test_points))
        
    def e(self, n): # blad bezwzgledny aproksymacji
        return sum(abs((p[1] - self.w(p[0], n)) / p[1])  for p in self.points) / len(self.points)

    def get_data_e_function(self, data):
        return lambda n: sum(abs((p[1] - self.w(p[0], n)) / p[1]) for p in data) / len(data)

    def train(self, e_function):
        self.best_e, self.best_n = min(
            [(e_function(n), n) for n in range(2, self.max_n + 1)],
            key = lambda x: x[0]
        )
        self.w.clear_cache() # clear cache from non-effective n

    def __call__(self, x):
        return self.w(x, self.best_n)
