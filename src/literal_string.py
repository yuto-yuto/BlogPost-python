from typing import Dict, get_args, Literal
from enum import Enum

roles_str = ["manager", "developer", "tester"]

role_ids_with_str: Dict[str, int] = {
    "manager": 1,
    "developer": 2,
    "tester": 3,
}


def get_role_id_with_str(role: str):
    if role in roles_str:
        print(f"ID ({role}): {role_ids_with_str[role]}")
    else:
        print(f"Role not found: {role}")


get_role_id_with_str("manager")
get_role_id_with_str("owner")


class Role(Enum):
    Manager = "manager"
    Developer = "developer"
    Tester = "tester"


role_ids_with_enum: Dict[Role, int] = {
    Role.Manager: 1,
    Role.Developer: 2,
    Role.Tester: 3,
}


def get_role_id_with_enum(role: Role):
    print(f"ID ({role.value}): {role_ids_with_enum[role]}")
    print(f"role: ({role}), name: {role.name}, value: {role.value}")


get_role_id_with_enum(Role.Manager)
# Argument of type "Literal['developer']" cannot be assigned to parameter "role" of type "Role" in function "get_role_id_with_enum"
# "Literal['developer']" is incompatible with "Role"
# get_role_id_with_enum("developer")

RolesLiteral = Literal["manager", "developer", "tester"]
role_ids_with_literal: Dict[RolesLiteral, int] = {
    "manager": 1,
    "developer": 2,
    "tester": 3,
}


def get_role_id_with_literal(role: RolesLiteral):
    print(f"ID ({role}): {role_ids_with_literal[role]}")


get_role_id_with_literal("manager")
# Argument of type "Literal['owner']" cannot be assigned to parameter "role" of type "roles_literal" in function "get_role_id_with_literal"
#   Type "Literal['owner']" cannot be assigned to type "roles_literal"
#     "Literal['owner']" cannot be assigned to type "Literal['manager']"
#     "Literal['owner']" cannot be assigned to type "Literal['developer']"
#     "Literal['owner']" cannot be assigned to type "Literal['tester']"
# get_role_id_with_literal("owner")


def get_literal_values():
    values = get_args(RolesLiteral)
    print(values)  # ('manager', 'developer', 'tester')
    dynamic_ids = {}
    for index, x in enumerate(values):
        dynamic_ids[x] = index + 1

    print(dynamic_ids) # {'manager': 1, 'developer': 2, 'tester': 3}


get_literal_values()
