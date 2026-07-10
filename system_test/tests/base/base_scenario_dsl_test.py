import pytest

from system_test.core.channels.channel_type import ChannelType
from system_test.core.scenario.impl.scenario_dsl_impl import ScenarioDslImpl
from system_test.core.use_case_dsl import UseCaseDsl


class BaseScenarioDslTest:
    """Base class for all scenario-DSL-based system tests.

    Handles creation and teardown of the UseCaseDsl application context,
    and exposes a scenario() factory method that mirrors the Java reference:

        protected IScenarioDsl Scenario(Channel channel) { ... }
        protected IScenarioDsl Scenario()               { ... }

    Usage
    -----
    class TestSystemSmoke(BaseScenarioDslTest):

        @channel(ChannelType.API, ChannelType.UI)
        def test_should_be_able_to_go_to_system(self):
            self.scenario().assume().system().should_be_running()
    """

    @pytest.fixture(autouse=True)
    def _setup(self):
        self._app = UseCaseDsl()
        yield
        self._app.close()

    def scenario(self, channel: ChannelType | None = None) -> ScenarioDslImpl:
        return ScenarioDslImpl(self._app)
