
# Space: O(1)
# Time: O(1)

import random

class Solution:

    def __init__(self, radius, x_center, y_center):
        self.x_center = x_center
        self.y_center = y_center
        self.x_top = x_center + radius
        self.x_bottom = x_center - radius
        self.y_top = y_center + radius
        self.y_bottom = y_center - radius
        self.radiusSquared = radius ** 2

    def randPoint(self):
        x_res = random.uniform(self.x_bottom, self.x_top)
        y_res = random.uniform(self.y_bottom, self.y_top)

        while (x_res - self.x_center) ** 2 + (y_res - self.y_center) ** 2 > self.radiusSquared:
            x_res = random.uniform(self.x_bottom, self.x_top)
            y_res = random.uniform(self.y_bottom, self.y_top)

        return [x_res, y_res]






