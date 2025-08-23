# Accounts

Types:

```python
from itellicoai.types import Account
```

Methods:

- <code title="get /v1/accounts/{account_id}">client.accounts.<a href="./src/itellicoai/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/itellicoai/types/account.py">Account</a></code>
- <code title="get /v1/accounts/me">client.accounts.<a href="./src/itellicoai/resources/accounts/accounts.py">retrieve_current</a>() -> <a href="./src/itellicoai/types/account.py">Account</a></code>

## Agents

Types:

```python
from itellicoai.types.accounts import (
    AgentResponse,
    AmbientSound,
    AnthropicModel,
    AzureStt,
    CheckIn,
    DeepgramStt,
    InitialMessage,
    InterruptSettings,
    Message,
    OpenAIModel,
    PronunciationRule,
    ResponseTiming,
    AgentListResponse,
)
```

Methods:

- <code title="post /v1/accounts/{account_id}/agents">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">create</a>(account_id, \*\*<a href="src/itellicoai/types/accounts/agent_create_params.py">params</a>) -> <a href="./src/itellicoai/types/accounts/agent_response.py">AgentResponse</a></code>
- <code title="get /v1/accounts/{account_id}/agents/{agent_uuid}">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">retrieve</a>(agent_uuid, \*, account_id) -> <a href="./src/itellicoai/types/accounts/agent_response.py">AgentResponse</a></code>
- <code title="patch /v1/accounts/{account_id}/agents/{agent_uuid}">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">update</a>(agent_uuid, \*, account_id, \*\*<a href="src/itellicoai/types/accounts/agent_update_params.py">params</a>) -> <a href="./src/itellicoai/types/accounts/agent_response.py">AgentResponse</a></code>
- <code title="get /v1/accounts/{account_id}/agents">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">list</a>(account_id, \*\*<a href="src/itellicoai/types/accounts/agent_list_params.py">params</a>) -> <a href="./src/itellicoai/types/accounts/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/agents/{agent_uuid}">client.accounts.agents.<a href="./src/itellicoai/resources/accounts/agents.py">delete</a>(agent_uuid, \*, account_id) -> None</code>
