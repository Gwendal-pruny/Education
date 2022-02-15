from .battle_util import PlayerHasDiedError

def run(battle):
    while True:
        battle.run_turn()

        if battle.fled:
            break

        if battle.player.entity.health == 0:
            raise PlayerHasDiedError

        if battle.enemy.health == 0:
            battle.print_player_message("victory")

            battle.player.entity.stamina = battle.player.entity.maximum_stamina
            battle.player.entity.mana = battle.player.entity.maximum_mana

            break
