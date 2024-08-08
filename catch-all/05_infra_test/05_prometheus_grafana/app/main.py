from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time

# Create metrics to track time spent, requests made, and other events.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')
UPDATE_COUNT = Counter('update_count', 'Number of updates')
ACTIVE_REQUESTS = Gauge('active_requests', 'Number of active requests')
REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency in seconds')

# Decorate function with metrics.


@REQUEST_TIME.time()
@REQUEST_LATENCY.time()
def process_request(t):
    """A dummy function that takes some time."""
    ACTIVE_REQUESTS.inc()
    time.sleep(t)
    ACTIVE_REQUESTS.dec()


def main():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("[*] Starting server on port 8000...")

    # Generate some requests.
    while True:
        msg = random.random()
        process_request(msg)
        update_increment = random.randint(1, 100)
        UPDATE_COUNT.inc(update_increment)
        print(
            f'[+] Processing request: {msg:.4f} | Updates: {update_increment}')
        time.sleep(random.uniform(0.5, 2.0))  # Random delay between requests


if __name__ == '__main__':
    main()
