from bedrock_agentcore.memory import MemoryClient

client = MemoryClient(region_name="us-east-1")

memory_id = client.create_memory (
	name = "test_memory_20261005",
	description = "Short-term memory only",
 	event_expiry_days = 15,
	)


