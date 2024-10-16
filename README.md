# NATS Multi-Language Application

This repository showcases the use of NATS as a lightweight, high-performance messaging system to facilitate communication between applications written in different languages and frameworks.

The aim is to demonstrate how NATS can seamlessly connect microservices across multiple languages—in this case, Node.js and Python—and allow them to interact in real-time through message-based communication.

## Overview

This project implements a simple client-server architecture using NATS:

- Node.js acts as a client, periodically sending requests to add two numbers.

- Python acts as a server, receiving these requests, performing the addition, and sending back the results after a random delay.

## Why Use NATS for Multi-Language Communication?

NATS is an excellent choice for microservices or multi-language distributed systems because it provides:

- **Low-latency, high-performance messaging**: NATS is designed for fast communication between services.

- **Language-agnostic messaging**: It supports numerous programming languages, making it an ideal tool for inter-service communication across languages like Node.js, Python, Go, Rust, and more.

- **Simple pub/sub and request/reply model**: This model makes it easy to set up asynchronous messaging or RPC (remote procedure calls) across different services.

- **Ease of Scaling**: As your system grows and you add more services, NATS easily scales to handle high loads of messages across distributed systems.

## Architecture

The project comprises the following components:

1. **NATS Server (via Docker)**: A NATS server instance is managed via Docker using docker-compose. This server acts as the message broker between different applications.

2. **Node.js Client**:

   - Periodically sends RPC requests to add two numbers.
   - Logs the request and response using Pino for structured and pretty-printed logs.

3. **Python Server**:
   - Listens for requests from NATS and processes them by adding two numbers.
   - Introduces a random delay (between 5 and 10 seconds) to simulate variable processing times.

## Getting Started

### Prerequisites

- **Docker & Docker Compose**: Ensure Docker is installed on your machine. Docker Compose is required to start the NATS server.

- **Node.js**: Install Node.js (v20 or above).

- **Python**: Install Python 3.11 (or above).

- **pnpm**: Install pnpm for managing Node.js dependencies.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jagreehal/nats-multi-language-app.git
   cd nats-multi-language-app
   ```

2. Start NATS using Docker Compose:

   ```bash
   docker-compose up -d
   ```

   This will start a NATS server with JetStream enabled on ports 4222 (NATS) and 8222 (HTTP management).

3. Install Node.js dependencies:

   ```bash
   cd node-app
   pnpm install
   ```

4. Install Python dependencies:

   ```bash
   cd python-app
   python3.11 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Running the Applications

You can use the Makefile at the root of the project to simplify running both applications:

- Start both Node.js and Python applications:

  ```bash
  make start
  ```

  This will:

  - Start the Node.js client (`npx tsx watch`).
  - Start the Python server (`pymon` for auto-reloading during development).

- Run individually:

  - Node.js Client:

    ```bash
    make start-ts
    ```

  - Python Server:

  ```bash
    make start-py
  ```

## How It Works

### Node.js Client (RPC Requester)

- Every 5 seconds, the Node.js client sends a request to the Python server using NATS.

- It uses a random UUID to identify each request and asks for the sum of 0.1 + 0.2.

- The request is sent to the NATS subject `rpc.add`.

- The client waits for a reply from the Python server and logs either the result or an error using Pino for structured logs.

### Python Server (RPC Responder)

- The Python server subscribes to the `rpc.add` subject on NATS and waits for incoming requests.

- Upon receiving a request, it simulates a delay of 5 to 10 seconds before processing the request.

- After processing the request (adding two numbers), the result is sent back to the Node.js client via NATS.

### Example Flow

1. The Node.js client sends a request to `rpc.add` with `num1: 0.1` and `num2: 0.2`.

2. The Python server receives the request, simulates a delay, adds the two numbers, and sends the result back.

3. The Node.js client logs the result once it's received.

## Why This Approach?

By using NATS for communication between different programming languages:

- **Interoperability**: It allows microservices written in different languages (like Node.js, Python, Go, Rust) to interact seamlessly.

- **Real-Time Communication**: NATS provides low-latency, real-time messaging for distributed systems.

- **Scalability**: This architecture can be easily scaled as you add more
  services or replace services with other languages/frameworks.

- **Flexibility**: Each service can be written in a language best suited for the task, making it possible to optimise each component for performance or ease of development.

## Coming Soon

- **More Languages**: Additional services in other languages like Go, Rust, or C# will be added to further demonstrate the flexibility of NATS in a multi-language architecture.

## License

This project is licenced under the MIT License.
