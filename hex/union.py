from .constants import BLACK, BLUE, RED

class Union:
    def __init__(self, row, col):
        self.arbres = [{"parent": i, "rank": 0, "color": BLACK} for i in range(row*col+4)]
        self.arbres[row*col]["color"] = BLUE
        self.arbres[row*col + 1]["color"] = BLUE
        self.arbres[row*col + 2]["color"] = RED
        self.arbres[row*col + 3]["color"] = RED

    def find(self, x):
        if self.arbres[x]["parent"] == x:
            return x
        return self.find(self.arbres[x]["parent"])

    def union(self, x, y):
        xRacine = self.find(x)
        yRacine = self.find(y)
        if (xRacine != yRacine
            and self.arbres[xRacine]["color"] == self.arbres[yRacine]["color"]):

            if self.arbres[xRacine]["rank"] < self.arbres[yRacine]["rank"]:
                self.arbres[xRacine]["parent"] = yRacine
            else:
                self.arbres[yRacine]["parent"] = xRacine
                if self.arbres[xRacine]["rank"] == self.arbres[yRacine]["rank"]:
                    self.arbres[xRacine]["rank"] += 1
