class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(node, visited):
            num_rooms_visited = 0
            visited.add(node)
            for room in rooms[node]:
                if room not in visited:
                    num_rooms_visited += 1
                    num_rooms_visited += dfs(room, visited)
            return num_rooms_visited

        return 1 + dfs(0, visited)== n
