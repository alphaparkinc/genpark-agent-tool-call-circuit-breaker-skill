import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentToolCallCircuitBreakerClient

def main():
    client = AgentToolCallCircuitBreakerClient()
    res = client.evaluate_circuit_state()
    print("=== Agent Tool Call Circuit Breaker Output ===")
    print(f"Tool: {res['primary_tool']} -> Fallback: {res['fallback_tool']}")
    print(f"Failures: {res['failure_count']}/{res['window_calls_evaluated']} (Rate: {res['failure_rate']*100}%) | Latency: {res['average_latency_ms']}ms")
    print(f"Circuit State: {res['circuit_state']} | Route: {res['active_execution_route']}")
    print(f"Directive: {res['action_directive']} (Backoff: {res['retry_backoff_seconds']}s)")

if __name__ == '__main__':
    main()
