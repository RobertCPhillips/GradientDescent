class Multiplier:
    def forward(self, x, y):
        z = x * y
        self.x = x
        self.y = y
        return z
    def backward(self, dz): #dz => dL/dz
        dx = self.y * dz # => dL/dx = dL/dz*dz/dx
        dy = self.x * dz # => dL/dy = dL/dz*dz/dy
        return [dx, dy]