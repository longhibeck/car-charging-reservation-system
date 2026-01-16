from typing import TypeVar, Any
from http import HTTPStatus
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.clients.typed_response import TypedResponse

T = TypeVar("T")


class HttpTestUtils:
    @staticmethod
    def get_ok_result_or_failure(response: TypedResponse[T]) -> Result[T]:
        return HttpTestUtils._get_result_or_failure(response, HTTPStatus.OK, True)

    @staticmethod
    def get_created_result_or_failure(response: TypedResponse[T]) -> Result[T]:
        return HttpTestUtils._get_result_or_failure(response, HTTPStatus.CREATED, True)

    @staticmethod
    def get_no_content_result_or_failure(response: TypedResponse[T]) -> Result[None]:
        return HttpTestUtils._get_result_or_failure(
            response, HTTPStatus.NO_CONTENT, False
        )

    @staticmethod
    def _get_result_or_failure(
        response: TypedResponse[T], status_code: HTTPStatus, has_data: bool
    ) -> Result[T]:
        if response.status_code == status_code:
            if has_data:
                return Result.success(response.json())
            return Result.success()
        return HttpTestUtils.extract_error_messages(response)

    @staticmethod
    def extract_error_messages(response: TypedResponse[Any]) -> Result[T]:
        data = response.json()
        if HttpTestUtils._is_problem_details(data):
   
            problem_details = data # as ProblemDetailResponse
            error_messages = []        

            if problem_details.get("detail"):
                error_messages.append(problem_details["detail"])

            if problem_details.get("title") and problem_details.get("title") != problem_details.get("detail"):
                error_messages.append(f"Title: {problem_details["title"]}")


            if problem_details.get("errors") and len(problem_details.get("errors")) > 0:
                for error in problem_details["errors"]:
                    error_messages.append(error.message)

            if not error_messages:
                return Result.failure(error_messages)

    @staticmethod
    def _is_problem_details(data: Any) -> bool:
        return data and (data.type or data.title or data.detail or data.errors)
