class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList: dict[int, List[int]] = {}
        visted = set()

        for preReq, course in prerequisites:
            if not preReq in adjList:
                adjList[preReq] = []
            if not course in adjList:
                adjList[course] = []
            adjList[preReq].append(course)

        def dfs(key: int) -> bool: # dfs for each element in the key
            if key in visted: # 
                return False
            if adjList[key] == []:
                return True

            visted.add(key)  # Will only contain 1 element aka key

            for course in adjList[key]:
                cycle = not dfs(course)
                if cycle:
                    return False
            visted.remove(key)
            adjList[key] = [] # clear all children so (almost like dynamic programming)
            
            return True
            
        for postReq, preReq in prerequisites:
            if not dfs(postReq):
                return False
        
        return True

            
            
            

        # turn to adj list

        # for each list see if dfs returns back to you
        