
def solution(sx, sy, x, y):
    diffs = [(2, 1), (1, 2), (2, -1), (-1, 2),
             (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    root = (sx, sy)
    desired = (abs(x), abs(y))
    q = [(root, 0)]
    visited = set(root)
    while True:
        coords, dist = q.pop(0)
        if coords == desired:
            return dist
        for nbr in [(coords[0] + a, coords[1] + b) for (a, b) in diffs]:
            if nbr not in visited and nbr[0] >= -2 and nbr[1] >= -2:
                q.append((nbr, dist + 1))
                visited.add(nbr)


print(solution(5, 1, 0, 5))
