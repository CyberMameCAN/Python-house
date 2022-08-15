"""ランダム・ウォークを計算するクラス


"""
from dataclasses import dataclass
import random
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class RandomWalk:
    _count: int = 25  # デフォルト値

    def __init__(self) -> None:
        pass

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, _count: int) -> None:
        self._count = _count

    def random_walk(self) -> list:
        direction: list = []
        #random.seed(24)
        for i in range(self._count):
            x = 1 if random.random() >= 0.5 else -1
            direction.append(x)
        return direction

    def positioning(self, direction: list) -> list:
        """cumsumと同じことをやっている"""

        x: list = []
        x_point: int = 0  # 現在地

        for dirc in direction:
            x_point = x_point + dirc
            x.append(x_point)

        return x

rw = RandomWalk()
rw.count: int = 50  # プロット数
kinds: int = 10  # 何種類作るか
directions: list = []
labels: list = []

for kind in range(kinds):
    direction = rw.random_walk()
    #position = rw.positioning(direction)  # cumsumあるの忘れてた
    cumsum_direction = np.cumsum(direction)
    cumsum_direction = np.append(0, cumsum_direction) # ゼロスタートとしたいので、先頭にゼロを追加
    directions.append(cumsum_direction)
    labels.append(f'Line{kind+1}')

plt.style.use('ggplot')
fig = plt.figure(figsize = (10,7))
#fig, ax = plt.subplots()
for kind in range(kinds):
    plt.plot(range(0, rw.count+1), directions[kind])

plt.ylim(-20, 20)
plt.legend(labels=labels, loc='best', borderaxespad=1, fontsize=12)
#plt.grid()
plt.title('Random Walk')
fig.tight_layout()
fig.savefig("random_walk.png")

#print(plt.style.available)