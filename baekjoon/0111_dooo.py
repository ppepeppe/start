a = list(input())
b = list(input())
lst = []
def dfs(start, ans):
    if ans == start:
        lst.append(1)
        return
    if len(ans) == 0:
        lst.append(0)
        return
    if ans[-1] == 'A':
        dfs(start, ans[:-1])
    if ans[0] == 'B':
        dfs(start, ans[1:][::-1])
result = dfs(a, b)
if sum(lst) >= 1:
    print(1)
else:
    print(0)