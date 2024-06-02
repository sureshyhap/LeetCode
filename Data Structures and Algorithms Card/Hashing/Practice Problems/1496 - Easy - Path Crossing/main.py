class Solution:
    def isPathCrossing(self, path: str) -> bool:
        previously_visited = set()
        current_position = [0, 0]
        previously_visited.add(tuple(current_position))
        for direction in path:
            if direction == "N":
                current_position[1] += 1
            elif direction == "S":
                current_position[1] -= 1
            elif direction == "E":
                current_position[0] += 1
            elif direction == "W":
                current_position[0] -= 1
            current_position_tuple = tuple(current_position)
            if current_position_tuple in previously_visited:
                return True
            previously_visited.add(current_position_tuple)
        return False
