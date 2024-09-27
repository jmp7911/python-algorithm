class Solution:
    def simplifyPath(self, path: str) -> str:
        be = ''
        path2 = []
        path += '/'
        for c in path:
            print(path2)
            if c == '/':
                if be == '..':
                    if len(path2) > 0:
                        path2.pop()
                elif be != '' and be != '.':
                    path2.append(be)
                be = ''
            elif c != '/':
                be += c
        
        return '/' + '/'.join(path2) if len(path2) > 0 else '/'