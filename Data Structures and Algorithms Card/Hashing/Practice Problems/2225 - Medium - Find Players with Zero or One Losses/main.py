class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        games_lost = {}
        for i, j in matches:
            if i not in games_lost:
                games_lost[i] = 0
            if j not in games_lost:
                games_lost[j] = 1
            else:
                games_lost[j] += 1

        answer = [[], []]
        for player, lost_games in games_lost.items():
            if lost_games == 0:
                answer[0].append(player)
            elif lost_games == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()

        return answer
