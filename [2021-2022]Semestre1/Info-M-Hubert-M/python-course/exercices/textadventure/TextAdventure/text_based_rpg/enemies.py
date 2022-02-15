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
        dexterity=20,
        composure=5,
        critical_hit_chance=2
    )

def maeva():
    return CombatEntity(
        display_name="maeva",
        attacks=[
            attack.Attack(
                name="Frappe",
                display_name="Frappe",
                type_=attack.MELEE,
                damage=5,
                description_of_being_used="frappe",
                stamina_cost=3
            ),
            attack.Attack(
                name="Finishim",
                display_name="finishim",
                type_=attack.MELEE,
                damage=12,
                description_of_being_used="FINISHIM",
                stamina_cost=8
            )
        ],
        maximum_health=40,
        maximum_stamina=20,
        strength=20,
        defence=20,
        dexterity=19,
        composure=10,
        critical_hit_chance=3
    )
    
def forgerone():
    return CombatEntity(
        display_name="forgerone",
        attacks=[
            attack.Attack(
                name="Forgage d'esprit",
                display_name="Hammer spirit inpulse",
                type_=attack.MELEE,
                damage=10,
                description_of_being_used="hammer spirit inpulse",
                stamina_cost=3
            ),
            attack.Attack(
                name="Hammer earthquakes",
                display_name="Hammer earthquakes",
                type_=attack.MELEE,
                damage=20,
                description_of_being_used="Hammer earthquakes",
                stamina_cost=4
            )
        ],
        maximum_health=70,
        maximum_stamina=30,
        strength=25,
        defence=25,
        dexterity=0,
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
                damage=15,
                description_of_being_used="lancé de craie",
                stamina_cost=10
            ),
            attack.Attack(
                name="Coup de règle en MÉTAL",
                display_name="Règle",
                type_=attack.MELEE,
                damage=20,
                description_of_being_used="coup de règle",
                stamina_cost=15
            )
        ],
        maximum_health=150,
        maximum_stamina=25,
        strength=30,
        defence=25,
        dexterity=0,
        composure=8,
        critical_hit_chance=2
    )
