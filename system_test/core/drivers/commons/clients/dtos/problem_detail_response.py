from typing import TypedDict, NotRequired, Any


class ProblemDetailsFieldErrorResponse(TypedDict):
    field: str
    message: str
    code: str
    rejected_value: Any


class ProblemDetailResponse(TypedDict):
    type: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[int]
    detail: NotRequired[str]
    instance: NotRequired[str]
    errors: NotRequired[list[ProblemDetailsFieldErrorResponse]]
