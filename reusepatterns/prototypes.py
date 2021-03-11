import copy


class PrototypeMixin:

    def copy(self):
        """Clone a registered object and update inner attributes dictionary"""
        return copy.deepcopy(self)

