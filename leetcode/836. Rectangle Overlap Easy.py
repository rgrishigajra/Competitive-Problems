class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 0=x1, 1=x2, 2=y1,3=y2
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or
                rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
