class Constants:
    """
    Static class that allows access to constant values
    """

    WIDTH = 1000
    HEIGHT = 700
    WIN_EDGE_FROM_SUN = 6 # how many AUs is the Edge of the window
    trailLength = 15
    
    trailstart = 365
    TRAIL =  trailstart - trailLength
    AU = 149597870700
    G = 6.67430e-11
    SCALE = WIDTH / 2 / WIN_EDGE_FROM_SUN / AU # Sets AU to pixels
    TIMESTEP = 3600 * 24 # 1 Day


class Color:
    """
    Static class that allows defined rgb colors.
    """

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 120, 0)
    GREY = (200, 200, 200)