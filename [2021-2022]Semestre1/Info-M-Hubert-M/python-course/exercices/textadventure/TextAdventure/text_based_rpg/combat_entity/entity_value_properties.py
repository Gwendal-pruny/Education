def generate_value_property(name):

    @property
    def value_property(entity):
        return getattr(entity, "_" + name)

    @value_property.setter
    def value_property(entity, value):
        value_maximum = getattr(entity, "maximum_" + name)

        if value > value_maximum:
            value = value_maximum

        if value < 0:
            value = 0

        setattr(entity, "_" + name, value)

    return value_property

def generate_maximum_value_stat_property(name):

    @property
    def maximum_value_stat_property(entity):
        return getattr(entity, "_maximum_" + name)

    @maximum_value_stat_property.setter
    def maximum_value_stat_property(entity, value):
        setattr(entity, "_maximum_" + name, value)

        if not hasattr(entity, name) or value < getattr(entity, name):
            setattr(entity, name, value)

    return maximum_value_stat_property
