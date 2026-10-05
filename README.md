# BuildingAgenticOct52026

## Class links

- [Access to labs and courseware](https://us-east-1.student.classrooms.aws.training/class/ilt%23aRZaLdfBWfAFjabuiuRqQ5). This is a direct link to the class. There are two other paths to get there:
    - https://classrooms.aws.training : here you can see all the classes you have signed up for.
    - https://myclass.skillbuilder.aws/ : here you see current and past classes. Once the class is marked as complete (early afternoon), it moves to the past classes. There, you will be able to fill the evaluation survey.
- [2025 Top 10 Risk & Mitigations for LLMs and Gen AI Apps](https://genai.owasp.org/llm-top-10/)

- [What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [REAC T: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS](https://arxiv.org/pdf/2210.03629)
- [Introducing Amazon Bedrock Managed Knowledge Base for faster, more accurate enterprise AI applications](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications/)
- Interacting with a knowledge base via the API is done with two calls:
    - [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html), just pull related documents from the KB
    - [Retrieve and Generate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html), gets the documents and generates the augmented response
- [AgentCore regional availability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)
- [Amazon Bedrock AgentCore payments is now generally available: Enabling agents to transact safely and autonomously at scale](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/)
- [Manage agents, tools and skills at scale with AWS Agent Registry](https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/)
- [MCP reference registry](https://github.com/modelcontextprotocol/registry)
- [Amazon Bedrock AgentCore harness is now generally available: Go from idea to production-grade agent in minutes](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/)
- Evaluations
    - [Programmatic](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-evaluation-prompt-datasets-builtin.html)
    - [RAGAS built-in metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
    - [Built-in metric evaluator prompts for model-as-a-judge evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html)
- Policy
    - [Why Policy in Amazon Bedrock AgentCore chose Cedar for securing agentic workflows](https://aws.amazon.com/blogs/security/why-policy-in-amazon-bedrock-agentcore-chose-cedar-for-securing-agentic-workflows/)
    - [Understanding Cedar policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-understanding-cedar.html)
- Frameworks
    - [Building a LangGraph Agent from Scratch](https://towardsdatascience.com/building-a-langgraph-agent-from-scratch/)
    - [CrewAI quickstart](https://docs.crewai.com/v1.15.18/en/quickstart)
    - [Langchain agents](https://docs.langchain.com/oss/python/langchain/agents)
    - [Langchain vector store integrations](https://docs.langchain.com/oss/python/integrations/vectorstores). It is not about vector stores, this is just one example of the amount of integrations available with Langchain
    - Strands
        - [Strands Agents SDK: A technical deep dive into agent architectures and observability](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)
        - [Strands tools](https://github.com/strands-agents/tools), community-driven set of tools
        - [Strands vended tools](https://strandsagents.com/docs/user-guide/sdk/tools/vended-tools/), "official set of tools"
        - [Strands hooks](https://strandsagents.com/docs/user-guide/sdk/agents/hooks-events/)

- [Runtime instances: persistent compute for production AI agents on Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/aws/runtime-instances-persistent-compute-for-production-ai-agents-on-amazon-bedrock-agentcore/)
- [Get started with Amazon Bedrock AgentCore Runtime direct code deployment](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy.html)
- Deployment toolset
    - [Agentcore CLI](https://github.com/aws/agentcore-cli)
    - **DEPRECATED** [Agentcore starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit)

- Memory
    - [Memory concepts in langchain doc](https://docs.langchain.com/oss/python/concepts/memory)
    - [Memory in the Age of AI Agents: A Survey](https://arxiv.org/pdf/2512.13564) - interesting research on agentic memory evolution and future

    - AgentCore
        - [Built-in long-term memory strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-strategies.html). Pay attention to the system prompts used in each strategy.
        - [Use short-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-memory-short-term.html), operations available are:
            - CreateEvent
            - GetEvent
            - ListEvents
            - DeleteEvent
        - [Use long-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-memory-long-term.html), operations available are:
            - [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html)
            - [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html)
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [MCP architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [Agentcore gateway targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-mcp.html)
- [Search for tools in your AgentCore gateway with a natural language query](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-semantic-search.html)