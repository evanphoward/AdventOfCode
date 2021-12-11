# Perhaps an excessively complicated OO approach, but a bit of fun and results in fairly clean dijkstra at the bottom
import heapq
import itertools
SPELL_COSTS = {"missile": 53, "drain": 73, "shield": 113, "poison": 173, "recharge": 229}
EFFECT_DURATIONS = {"shield": 6, "poison": 6, "recharge": 5}
BOSS_INIT_HP, BOSS_DMG = tuple(int(line.split()[-1]) for line in open("input").read().split("\n"))


class Game:
    def __init__(self, player=None, boss=None, player_turn=True, effects=None):
        self.player = player if player else Player()
        self.boss = boss if boss else Boss()
        self.playerTurn = player_turn
        self.effects = effects if effects else []

    def __str__(self):
        boss_stats = f"Boss HP: {self.boss.hp}"
        player_stats = f"Player HP: {self.player.hp} \t Player Mana: {self.player.mana} \t Player Armor: {self.player.armor}"
        effects = '\t'.join(f"{effect.name} {effect.duration}" for effect in self.effects)
        turn_text = "It is now the " + ("Player's" if self.playerTurn else "Boss'") + " turn"
        return f"{boss_stats} \n {player_stats} \n {effects} \n {turn_text}"

    def cast_spell(self, spell_name):
        self.player.change_mana(-SPELL_COSTS[spell_name])
        if self.player.mana <= 0:
            return False
        if spell_name == "missile":
            self.boss.receive_damage(4)
        elif spell_name == "drain":
            self.boss.receive_damage(2)
            self.player.heal(2)
        else:
            if spell_name in [effect.name for effect in self.effects]:
                return False
            self.effects.append(Effect(spell_name))
        return True

    def apply_effects(self):
        new_effects = []
        for effect in self.effects:
            if effect.apply_effect(self.player, self.boss) > 0:
                new_effects.append(effect)
        self.effects = new_effects

    def play_turn(self, spell_name=None, p2=False):
        game_copy = Game(self.player.copy(), self.boss.copy(), not self.playerTurn, [effect.copy() for effect in self.effects])
        if p2:
            game_copy.player.hp -= 1
            if game_copy.player.hp <= 0:
                return False
        game_copy.apply_effects()
        if game_copy.is_win():
            return game_copy
        if self.playerTurn:
            if not game_copy.cast_spell(spell_name):
                return False
        else:
            if not game_copy.boss.attack(game_copy.player):
                return False
        return game_copy

    def is_win(self):
        return self.boss.hp <= 0


class Effect:
    def __init__(self, name, duration=None):
        self.name = name
        self.duration = duration if duration else EFFECT_DURATIONS[name]

    def apply_effect(self, player, boss):
        if self.name == "shield":
            player.armor = 7
        elif self.name == "poison":
            boss.receive_damage(3)
        elif self.name == "recharge":
            player.change_mana(101)
        self.duration -= 1
        return self.duration

    def copy(self):
        return Effect(self.name, self.duration)


class Player:
    def __init__(self, hp=50, mana=500):
        self.hp = hp
        self.mana = mana
        self.armor = 0

    def receive_damage(self, dmg):
        self.hp -= (dmg - self.armor)

    def change_mana(self, mana_amt):
        self.mana += mana_amt

    def heal(self, heal_amt):
        self.hp += heal_amt

    def copy(self):
        return Player(self.hp, self.mana)


class Boss:
    def __init__(self, hp=BOSS_INIT_HP):
        self.hp = hp
        self.dmg = BOSS_DMG

    def attack(self, player):
        player.receive_damage(self.dmg)
        return player.hp > 0

    def receive_damage(self, dmg):
        self.hp -= dmg

    def copy(self):
        return Boss(self.hp)


def dijkstra(p2):
    initial_game_state = Game()
    counter = itertools.count()
    dijkstra_q = [(0, next(counter), initial_game_state, [])]
    while dijkstra_q:
        mana_used, _, game_state, spells_used = heapq.heappop(dijkstra_q)
        for spell in ["missile", "drain", "shield", "poison", "recharge"]:
            next_game_state = game_state.play_turn(spell, p2)
            if next_game_state:
                if next_game_state.is_win():
                    return mana_used + SPELL_COSTS[spell]
                next_game_state = next_game_state.play_turn()
                if next_game_state:
                    if next_game_state.is_win():
                        return mana_used + SPELL_COSTS[spell]
                    heapq.heappush(dijkstra_q, (mana_used + SPELL_COSTS[spell], next(counter), next_game_state, spells_used + [spell]))


print("Part 1:", dijkstra(False))
print("Part 2:", dijkstra(True))
