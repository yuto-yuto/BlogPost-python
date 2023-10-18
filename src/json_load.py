import json
from types import SimpleNamespace
from typing import Any, Dict, List


class Version:
    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch


class Software:
    def __init__(
        self,
        name: str,
        version: Dict[str, Any],
        availableVersions: List[str],
    ) -> None:
        self.name = name
        self.version = Version(**version)
        # self.version = version
        self.available_versions = availableVersions


def run():
    version_info = {
        "major": 2,
        "minor": 1,
        "patch": 0,
    }

    software_info = {
        "name": "my-software",
        "version": version_info,
        "availableVersions": ["2.1.0", "2.0.0", "1.0.0"],
    }

    version_json = json.dumps(version_info, indent=2)
    print(version_json)
    # {
    #   "major": 2,
    #   "minor": 1,
    #   "patch": 0
    # }

    software_json = json.dumps(software_info, indent=2)
    print(software_json)
    # {
    #   "name": "my-software",
    #   "version": {
    #     "major": 2,
    #     "minor": 1,
    #     "patch": 0
    #   },
    #   "availableVersions": [
    #     "2.1.0",
    #     "2.0.0",
    #     "1.0.0"
    #   ]
    # }

    version_dict = json.loads(version_json)
    print(version_dict)
    # {'major': 2, 'minor': 1, 'patch': 0}
    print(
        f"major: {version_dict['major']}, minor: {version_dict.get('minor')}, patch: {version_dict.get('patch')}"
    )
    # major: 2, minor: None, patch: 0
    print(version_dict.get("unknown", 11))
    # 11

    version_obj = json.loads(version_json, object_hook=lambda d: SimpleNamespace(**d))
    print(
        f"major: {version_obj.major}, minor: {version_obj.minor}, patch: {version_obj.patch}"
    )
    # major: 2, minor: 1, patch: 0

    version = Version(**version_dict)
    # IntelliSense works here
    print(f"major: {version.major}, minor: {version.minor}, patch: {version.patch}")
    # major: 2, minor: 1, patch: 0

    software_obj = json.loads(software_json, object_hook=lambda d: SimpleNamespace(**d))
    print(f"name: {software_obj.name}")
    print(
        f"version: {software_obj.version}, version.major: {software_obj.version.major}"
    )
    print(
        f"availableVersions: {software_obj.availableVersions}, availableVersions[1]: {software_obj.availableVersions[1]}"
    )

    software_dict = json.loads(software_json)
    software = Software(**software_dict)
    print(f"name: {software.name}")
    # print(f"version: {isinstance( software.version,dict)}")
    print(f"version: {software.version}, version.major: {software.version.major}")
    print(
        f"availableVersions: {software.available_versions}, availableVersions[1]: {software.available_versions[1]}"
    )


run()
