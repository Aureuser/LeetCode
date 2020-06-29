class Solution:
    def simplifyPath(self, path):
        if path.__len__() < 2:
            return path
        dir_list = []
        for i in path.split('/'):
            if not i or i == '.':
                continue
            elif i == '..' and dir_list:
                dir_list.pop()
            elif i != '..' and i != '.':
                dir_list.append(i)
        return '/'+'/'.join(dir_list)

if __name__ == '__main__':
    solution = Solution()
    path = solution.simplifyPath('/../')
    # /
    print(path)
    path = solution.simplifyPath('/a//b////c/d//././/..')
    # / a / b / c
    print(path)
    path = solution.simplifyPath('/a/../../b/../c//.//')
    # / c
    print(path)