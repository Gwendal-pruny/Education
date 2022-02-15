from .data import DATA

@property
def evasion(entity):
    value = entity.dexterity + entity.composure

    if entity.stamina <= entity.maximum_stamina / 10:
        value /= 2

    return round(value)
@property
def usable_attacks(entity):
    usable_attacks_list = []

    for entity_attack in entity.attacks:
        if (
                entity.stamina >= entity_attack.stamina_cost and \
                entity.mana >= entity_attack.mana_cost
        ):
            usable_attacks_list.append(entity_attack)

    return usable_attacks_list

@property
def values_view(entity):
    lines = []

    for value_name in DATA["entity_values"]:
        value = getattr(entity, value_name)
        value_maximum_stat = getattr(entity, "maximum_" + value_name)

        if value_maximum_stat:
            lines.append(
                DATA["values_view_line_template"].format(
                    value_name=value_name.capitalize(),
                    current=value,
                    maximum=value_maximum_stat
                )
            )

    return "\n".join(lines)
