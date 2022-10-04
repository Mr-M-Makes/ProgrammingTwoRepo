import random as rm
import pygame as pg
import copy


class Sorter:
    def __init__(self, settings):
        self.settings = settings
        self.sorting = False
        self.sorts = []
        self.setup_sorts()

    def setup_sorts(self):
        values = []
        for _ in range(self.settings.number_of_values):
            height = rm.randint(1, self.settings.value_height)
            rectangle = Value(height, self.settings.value_width, pg.Color("grey"))
            values.append(rectangle)
        
        self.sorts.clear()
        self.sorts.append(Bubble_Sort(values))
        self.sorts.append(Selection_Sort(values))
        self.sorts.append(Insertion_Sort(values))

class Sort:
    def __init__(self, values):
        self.values = copy.deepcopy(values)
        self.sorting = True
        self.generator = self.sort()

    def draw(self, screen, x, y, padding):
        for rectangle in self.values:
            rectangle.draw(screen, x, y)
            x += rectangle.width + padding


class Bubble_Sort(Sort):
    def __init__(self, values):
        Sort.__init__(self, values)

    def sort(self):
        done = False
        sorted = 0

        while not done:
            yield True  #############
            done = True
            self.values[-sorted - 1].color = pg.Color("grey")  ############# 
            for k in range(len(self.values) - sorted - 1):
                yield True
                if k > 0:  #############
                    self.values[k - 1].color = pg.Color("grey")  ############# 
                self.values[k].color = pg.Color("yellow")  #############
                self.values[k + 1].color = pg.Color("cyan")  #############
                if self.values[k].height > self.values[k + 1].height:
                    yield True  #############                    
                    self.values[k], self.values[k + 1] = self.values[k + 1], self.values[k]
                    done = False
            sorted += 1
            self.values[-sorted].color = pg.Color("green")  ############# 

        if sorted < len(self.values):  #############
            yield True  #############
            for i in range(len(self.values) - sorted):  #############
                self.values[i].color = pg.Color("green")  #############
        yield False  #############


class Selection_Sort(Sort):
    def __init__(self, values):
        Sort.__init__(self, values)

    def sort(self):
        for i in range(len(self.values)):
            yield True  #############
            best = i
            self.values[-1].color = pg.Color("grey")  #############
            self.values[i].color = pg.Color("yellow")  #############
            for j in range(i + 1, len(self.values)):
                yield True  #############
                if j - 1 > i and j - 1 != best:  #############
                    self.values[j - 1].color = pg.Color("grey")  #############
                self.values[j].color = pg.Color("cyan")  #############
                if self.values[j].height < self.values[best].height:
                    if best != i:  #############
                        self.values[best].color = pg.Color("grey")  #############
                    best = j
                    if best != i:  #############
                        self.values[best].color = pg.Color("red")  #############
            yield True  #############
            self.values[i], self.values[best] = self.values[best], self.values[i]
            self.values[i].color = pg.Color("green")  #############
            if best != i:
                self.values[best].color = pg.Color("grey")  #############
        yield False  #############


class Insertion_Sort(Sort):
    def __init__(self, values):
        Sort.__init__(self, values)

    def sort(self):        
        self.values[0].color = pg.Color("green")
        for j in range(1, len(self.values)):
            yield True  #############
            k = j - 1
            self.values[j].color = pg.Color("yellow")  #############
            while k >= 0 and self.values[k].height > self.values[k + 1].height:
                yield True  #############
                self.values[k].color = pg.Color("cyan")  #############
                yield True  #############
                self.values[k], self.values[k + 1] = self.values[k + 1], self.values[k]
                self.values[k + 1].color = pg.Color("green")  #############
                self.values[k].color = pg.Color("yellow")  #############
                k -= 1
            self.values[k + 1].color = pg.Color("green")  #############
        yield False  #############


class Value:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color        

    def draw(self, screen, x, y):

        pg.draw.rect(screen, self.color, [x, y - self.height, self.width, self.height])