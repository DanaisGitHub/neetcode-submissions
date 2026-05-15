class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        movements = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS,COLS=len(board),len(board[0])

        

        def dfs (i:int,cord:tuple[int,int],visited:set)->bool:
            x,y = cord
            if i >= len(word):
                return True

            if min(x,y) < 0 or x >= ROWS or y >= COLS:
                return False
            if (x,y) in visited:
                return False
            if board[x][y] != word[i]:
                return False

            
            visited.add((x,y))
            ret:bool = False
            for mx,my in movements:
                newX,newY = mx+x,my+y
                ret = ret or dfs(i+1,(newX,newY),visited) # wont move until each movement processed
            
            # why remove
            visited.remove((x,y))
            return ret

        ret=False
        setVar = set()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    ret = ret or dfs(0,(r,c),set())
        
        return ret

            
        
        
        # linear search for start of word
        # set of dfs once found        