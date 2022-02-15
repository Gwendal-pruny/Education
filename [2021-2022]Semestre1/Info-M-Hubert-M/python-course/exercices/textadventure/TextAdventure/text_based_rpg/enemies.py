from .combat_entity import CombatEntity
from . import attack

def monstre():
    return CombatEntity(
        display_name="monstre",
        attacks=[
            attack.Attack(
                name="slash",
                display_name="Slash",
                type_=attack.MELEE,
                damage=2,
                description_of_being_used="slashe",
                stamina_cost=4
            ),
            attack.Attack(
                name="bite",
                display_name="Bite",
                type_=attack.MELEE,
                damage=4,
                description_of_being_used="bite",
                stamina_cost=6
            )
        ],
        maximum_health=20,
        maximum_stamina=15,
        strength=8,
        defence=10,
        dexterity=4,
        composure=5,
        critical_hit_chance=2
    )

def maeva():
    return CombatEntity(
        display_name="maeva",
        attacks=[
            attack.Attack(
                name="slash",
                display_name="Slash",
                type_=attack.MELEE,
                damage=8,
                description_of_being_used="slashe",
                stamina_cost=3
            ),
            attack.Attack(
                name="punch dash",
                display_name="Punch dash",
                type_=attack.MELEE,
                damage=9,
                description_of_being_used="Punch dash",
                stamina_cost=4
            )
        ],
        maximum_health=40,
        maximum_stamina=20,
        strength=10,
        defence=15,
        dexterity=8,
        composure=7,
        critical_hit_chance=4
    )
    
def forgerone():
    return CombatEntity(
        display_name="forgerone",
        attacks=[
            attack.Attack(
                name="Coup de marteau",
                display_name="Hammer",
                type_=attack.MELEE,
                damage=5,
                description_of_being_used="Hammer",
                stamina_cost=3
            ),
            attack.Attack(
                name="Hammer earthquakes",
                display_name="Hammer earthquakes",
                type_=attack.MELEE,
                damage=10,
                description_of_being_used="Hammer earthquakes",
                stamina_cost=4
            )
        ],
        maximum_health=50,
        maximum_stamina=20,
        strength=12,
        defence=15,
        dexterity=8,
        composure=7,
        critical_hit_chance=4
    )

def proffeseur():
    return CombatEntity(
        display_name="Professeur",
        attacks=[
            attack.Attack(
                name="Lancé de craie",
                display_name="Craie",
                type_=attack.MELEE,
                damage=10,
                description_of_being_used="lancé de craie",
                stamina_cost=6
            ),
            attack.Attack(
                name="Coup de règle en MÉTAL",
                display_name="Règle",
                type_=attack.MELEE,
                damage=19,
                description_of_being_used="coup de règle",
                stamina_cost=8
            )
        ],
        maximum_health=100,
        maximum_stamina=50,
        strength=15,
        defence=25,
        dexterity=7,
        composure=8,
        critical_hit_chance=15
    )
