from typing import Any, Dict, List, Literal, TypedDict, Union

from typing_extensions import Required

Action = Union["ShellAction", "TokenAction", "ActorAction"]
"""
action.

Aggregation type: oneOf
"""


ActorAction = Dict[str, Any]
"""
actor action.

a custom action
"""


CommandTokens = Dict[str, List[str]]
"""
command tokens.

command tokens which may be expanded as paths
"""


class DoitomlMetadata(TypedDict, total=False):

    """doitoml Metadata."""

    cwd: Required[str]

    env: "EnvironmentVariables"

    log: Required[List["_DefinitionsDoitomlLogItem"]]

    skip: Union[str, Union[int, float], None, Dict[str, Any]]

    source: Required[str]
    """ Required property """
    """
    environment variables.

    environment variables shared among all tasks
    """
    """ Required property """
    """ Aggregation type: oneOf """
    """ Required property """


class DoitomlSchema(TypedDict, total=False):

    """doitoml schema.

    schema for ``doitoml`` configuration
    """

    env: Required["EnvironmentVariables"]

    paths: Required["PathTokens"]

    tasks: Required[Dict[str, "Task"]]

    templates: Dict[str, Any]

    tokens: Required["CommandTokens"]
    """
    environment variables.

    environment variables shared among all tasks

    Required property
    """
    """
    path tokens.

    paths to expand and normalize, relative to the current working directory

    Required property
    """
    """ Required property """
    """ extensible task generators """
    """
    command tokens.

    command tokens which may be expanded as paths

    Required property
    """


EnvironmentVariables = Dict[str, str]
"""
environment variables.

environment variables shared among all tasks
"""


class Metadata(TypedDict, total=False):

    """Metadata."""

    doitoml: "DoitomlMetadata"
    """ doitoml Metadata. """


PathTokens = Dict[str, List["_DefinitionsArrayOfPathsItem"]]
"""
path tokens.

paths to expand and normalize, relative to the current working directory
"""


ShellAction = str
""" shell action. """


class Task(TypedDict, total=False):

    """Task."""

    actions: List["Action"]
    calc_dep: List["_DefinitionsArrayOfPathsItem"]
    doc: str
    file_dep: List["_DefinitionsArrayOfPathsItem"]
    meta: "Metadata"

    name: str
    targets: List["_DefinitionsArrayOfPathsItem"]
    title: str
    uptodate: List["Uptodate"]
    verbosity: "_TaskVerbosity"
    watch: List["_DefinitionsArrayOfPathsItem"]
    """ Metadata. """


TokenAction = List[str]
""" token action. """


Uptodate = Union[bool, str, Dict[str, Any], None]
"""
uptodate.

Aggregation type: oneOf
"""


_DefinitionsArrayOfPathsItem = str
""" minLength: 1 """


_DefinitionsDoitomlLogItem = Union[str, None]
""" Aggregation type: oneOf """


_TaskVerbosity = Union[Literal[1], Literal[2], Literal[3]]
_TASKVERBOSITY_1: Literal[1] = 1
"""The values for the '_TaskVerbosity' enum"""
_TASKVERBOSITY_2: Literal[2] = 2
"""The values for the '_TaskVerbosity' enum"""
_TASKVERBOSITY_3: Literal[3] = 3
"""The values for the '_TaskVerbosity' enum"""
