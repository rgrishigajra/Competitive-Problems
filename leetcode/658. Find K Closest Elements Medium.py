class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return [] 
        l, h = 0,len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==x:
                l = mid+1
                h = mid
                break
            elif arr[mid]>x:
                h = mid-1
            else:
                l = mid+1
        l,h=h,l
        d = deque()
        while l>=0 and h<len(arr) and len(d)!=k:
            if abs(arr[l]-x) <= abs(arr[h]-x): 
                d.appendleft(arr[l])
                l-=1
            else:
                d.append(arr[h])
                h+=1
        while l>=0 and len(d)!=k:
            d.appendleft(arr[l])
            l-=1
        while h<len(arr) and len(d)!=k:
            d.append(arr[h])
            h+=1
        return d