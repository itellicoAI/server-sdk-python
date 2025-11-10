# Accounts

Types:

```python
from itellicoai.types import Account
```

## Agents

Types:

```python
from itellicoai.types.accounts import (
    AgentResponse,
    AmbientSound,
    AnthropicModel,
    InitialMessage,
    InterruptSettings,
    OpenAIModel,
    ResponseTiming,
    AgentListResponse,
)
```

Methods:

- <code title="post /v1/accounts/{account_id}/agents">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">create</a>(account_id, \*\*<a href="src/itellicoai/types/accounts/agent_create_params.py">params</a>) -> <a href="./src/itellicoai/types/accounts/agent_response.py">AgentResponse</a></code>
- <code title="get /v1/accounts/{account_id}/agents">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">list</a>(account_id, \*\*<a href="src/itellicoai/types/accounts/agent_list_params.py">params</a>) -> <a href="./src/itellicoai/types/accounts/agent_list_response.py">AgentListResponse</a></code>
