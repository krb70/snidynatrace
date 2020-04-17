import oneagent
import atexit

from .log import logger

sdk = None


def shutdown():
    oneagent.shutdown()


def init(forkable=False):
    global sdk
    try:
        oneagent.initialize(forkable=forkable)
    except TypeError:
        # older versions of the oneagent SDK don't support forkable
        oneagent.initialize()
    state = oneagent.get_sdk().agent_state
    logger.debug("Initialized snidynatrace with AgentState: {}".format(state))
    if state != oneagent.common.AgentState.ACTIVE:
        logger.warning("Could not initialize the OneAgent SDK, AgentState: {}".format(state))

    atexit.register(shutdown)
    sdk = oneagent.get_sdk()
