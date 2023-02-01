from typing import Literal
from enum import Enum

roles_str = ["manager", "developer", "tester"]

role_ids_with_str: dict[str, int] = {
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


role_ids_with_enum: dict[Role, int] = {
    Role.Manager: 1,
    Role.Developer: 2,
    Role.Tester: 3,
}


def get_role_id_with_enum(role: Role):
    print(f"ID ({role}): {role_ids_with_enum[role]}")


get_role_id_with_enum(Role.Manager)
# Argument of type "Literal['owner']" cannot be assigned to parameter "role" of type "Role" in function "get_role_id_with_enum"
# "Literal['owner']" is incompatible with "Role"
# get_role_id_with_enum("owner")

roles_literal = Literal["manager", "developer", "tester"]


def get_role_id_with_literal(role: roles_literal):
    print(f"ID ({role}): {role_ids_with_str[role]}")


get_role_id_with_literal("manager")
# Argument of type "Literal['owner']" cannot be assigned to parameter "role" of type "roles_literal" in function "get_role_id_with_literal"
#   Type "Literal['owner']" cannot be assigned to type "roles_literal"
#     "Literal['owner']" cannot be assigned to type "Literal['manager']"
#     "Literal['owner']" cannot be assigned to type "Literal['developer']"
#     "Literal['owner']" cannot be assigned to type "Literal['tester']"
# get_role_id_with_literal("owner")

