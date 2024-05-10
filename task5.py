class hesab():
    def __init__(self):
        self.num_list = [2, 3, 4, 1, 8]

    def get_num(self, target_value):
        pairs = []
        for i in range(len(self.num_list)):
            for j in range(i+1, len(self.num_list)):
                if self.num_list[i] + self.num_list[j] == target_value:
                    pairs.append((i, j))
        if not pairs:
            return -1
        return pairs

Hesab = hesab()
print(Hesab.get_num(5))