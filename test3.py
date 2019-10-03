"""
3. The LeagueTable class tracks the score of each player in a league. After each game, the player records their score
with the record_result function.The player's rank in the league is calculated using the following logic:
 * The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
 * If two players are tied on score, then the player who has played the fewest games is ranked higher.
 * If two players are tied on score and number of games played, then the player who was first in the list of players is
 ranked higher.

Implement the player_rank function that returns the player at the given rank.

For example:
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before
Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".
"""


class LeagueTable:
    """Класс отслеживает счет каждого игрока в лиге."""
    def __init__(self, players: list):
        self.players = {player: {'counter_game': 0, 'score': 0} for player in players}

    def record_result(self, player: str, score: int):
        """Запись набранных очков игрока и инкримент счетчика игр."""
        self.players[player]['score'] += score
        self.players[player]['counter_game'] += 1

    def player_rank(self, place):
        """Выводит игрока, по переданному месту в таблице."""
        return sorted(self.players, key=lambda plr: (self.players[plr]['score'], self.players[plr]['counter_game']))[place-1]


if __name__ == '__main__':
    table = LeagueTable(['Майк', 'Крис', 'Арнольд'])
    table.record_result('Майк', 2)
    table.record_result('Майк', 3)
    table.record_result('Арнольд', 5)
    table.record_result('Крис', 5)
    print(table.player_rank(1))
