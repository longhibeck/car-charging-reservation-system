from uuid import uuid4


class UseCaseContext:
    """Shared scratchpad passed through every use-case execution.

    Two kinds of named entries:
    - *params*  – inputs the test seeds; auto-generated if absent so aliases are
                  always unique across test runs.
    - *results* – outputs captured after execute(); chained use cases read them
                  via get_result_value().
    """

    def __init__(self) -> None:
        self._params: dict[str, str] = {}
        self._results: dict[str, str] = {}
        self._failed_results: set[str] = set()

    # ------------------------------------------------------------------
    # Params (test → use case)
    # ------------------------------------------------------------------

    def get_param_value(self, alias: str) -> str:
        """Return the param value for *alias*, auto-generating one if missing."""
        if not alias or not alias.strip():
            return alias
        if alias not in self._params:
            self._params[alias] = f"{alias}-{uuid4().hex[:8]}"
        return self._params[alias]

    def set_param(self, alias: str, value: str) -> None:
        self._params[alias] = value

    # ------------------------------------------------------------------
    # Results (use case → use case / assertion)
    # ------------------------------------------------------------------

    def set_result_entry(self, alias: str, value: str) -> None:
        if not alias or not alias.strip():
            raise ValueError("Alias cannot be null or blank")
        if alias in self._results:
            raise ValueError(f"Alias already exists: '{alias}'")
        self._results[alias] = value
        self._failed_results.discard(alias)

    def set_result_entry_failed(self, alias: str, error: str) -> None:
        if not alias or not alias.strip():
            raise ValueError("Alias cannot be null or blank")
        self._results[alias] = f"FAILED: {error}"
        self._failed_results.add(alias)

    def get_result_value(self, alias: str) -> str:
        if not alias or not alias.strip():
            return alias
        value = self._results.get(alias)
        if value is None:
            return alias  # treat as literal when not yet stored
        if alias in self._failed_results:
            raise ValueError(
                f"Cannot get result value for alias '{alias}' "
                f"because the operation failed: {value}"
            )
        return value

    def expand_aliases(self, message: str) -> str:
        """Replace alias tokens inside *message* with their stored values."""
        for alias, value in {**self._params, **self._results}.items():
            message = message.replace(alias, value)
        return message
