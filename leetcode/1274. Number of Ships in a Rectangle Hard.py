# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def d_c(bottom, top):
            if bottom.x > top.x or bottom.y > top.y:
                return 0
            if (top.x, top.y) == (bottom.x, bottom.y):
                return int(sea.hasShips(top, bottom))
            else:
                if not sea.hasShips(top, bottom):
                    return 0
                x0, y0 = bottom.x, bottom.y
                x1, y1 = top.x, top.y
                center_x, center_y = (x0+x1)//2, (y0+y1)//2
                f1 = d_c(bottom, Point(center_x, center_y))
                f2 = d_c(Point(center_x+1, center_y+1), top)
                f3 = d_c(Point(x0, center_y+1), Point(center_x, y1))
                f4 = d_c(Point(center_x+1, y0), Point(x1, center_y))
                return f1+f2+f3+f4
        return d_c(bottomLeft, topRight)
