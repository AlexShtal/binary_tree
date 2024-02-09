from math import log


class Nod:
    """Создает узел в бинарном дереве"""
    global nods

    def __init__(self, pos: list, val: int):
        """Инициализирует атрибуты"""
        self.pos = pos
        self.val = val
        self.left_pos = [pos[0] + 1, (pos[1] - 1) * 2 + 1]
        self.right_pos = [pos[0] + 1, pos[1] * 2]

        """Проверяем если у узла корень"""
        if pos[0] == 1:
            self.head_pos = 'Not exist'
        else:
            self.head_pos = [pos[0] - 1, (pos[1] - 1) // 2 + 1]

    def val_set(self, val):
        """Присваивает вес"""
        self.val = val

    def val_get(self):
        """Возвращает вес"""
        return self.val

    def pos_get(self):
        """Возвращет координаты"""
        return self.pos

    def neighbors_val_get(self, name):
        """Принимает название соседа: 'head, left, right', возвращает его вес"""
        if name == 'head':
            return Nod.get_val(self.head_pos)
        elif name == 'left':
            return Nod.get_val(self.left_pos)
        elif name == 'right':
            return Nod.get_val(self.right_pos)
        else:
            print('Неверное введено название соседа узла')

    def neighbors_pos_get(self, name):
        """Получает название соседа: 'head, left, right', возвращает его координаты"""
        if name == 'head':
            return self.head_pos
        elif name == 'left':
            return self.left_pos
        elif name == 'right':
            return self.right_pos
        else:
            print('Неверное введено название соседа узла')

    def neighbors_get_all(self):
        """Возвращает информацию о всех соседних узлах"""
        return {
            'pos':
                {
                    'head': self.head_pos,
                    'left': self.left_pos,
                    'right': self.right_pos
                },
            'val':
                {
                    'head': Nod.get_val(self.head_pos),
                    'left': Nod.get_val(self.left_pos),
                    'right': Nod.get_val(self.right_pos)
                }

        }

    @staticmethod
    def find_nod(pos=None, val=None, head_val=None, right_val=None, left_val=None, head_pos=None,
                 right_pos=None,
                 left_pos=None):
        """Получает атрибуты, возвращает совпавший экземпляр"""
        for n in nods:
            if n.val_get() == val or n.pos_get() == pos or n.neighbors_val_get(
                    'head'
            ) == head_val or n.neighbors_val_get(
                'left'
            ) == left_val or n.neighbors_val_get('right') == right_val or n.neighbors_pos_get(
                'head'
            ) == head_pos or n.neighbors_pos_get('left') == left_pos or n.neighbors_pos_get('right') == right_pos:
                return n

    @staticmethod
    def get_val(nod_pos):
        """Получает координаты узла, возвращает его вес"""
        if nod_pos == 'Not exist':
            return 'Not exist'
        for nod_find in nods:
            if nod_find.pos_get() == nod_pos:
                return nod_find.val_get()
        else:
            return 'Not exist'


"""Получаем веса узлов"""

values = [int(i) for i in input('Введите значения узлов по порядку через запятую: ').split(',')]

"""Проектируем дерево"""

nods = []
cnt = 0
for i in range(1, int(log(len(values), 2) + 1) + 1):
    for j in range(1, 2 ** (i - 1) + 1):
        if cnt == len(values):
            break
        nods.append(Nod([i, j], values[(2 ** (i - 1) - 1) + j - 1]))
        cnt += 1

"""Тестируем и угараем"""
print('ТЕСТЫ:')
