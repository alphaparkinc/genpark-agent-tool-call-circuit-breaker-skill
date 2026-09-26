import json, sys
from client import AgentToolCallCircuitBreakerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "agent-tool-call-circuit-breaker", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "evaluate_circuit_state", "description": "Evaluates sliding tool-call error rates, trips circuit breakers, and routes to fallback tools."}]}}
    elif method == "tools/call":
        client = AgentToolCallCircuitBreakerClient()
        res = client.evaluate_circuit_state()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgentToolCallCircuitBreakerClient()
        print(json.dumps(client.evaluate_circuit_state(), indent=2))
