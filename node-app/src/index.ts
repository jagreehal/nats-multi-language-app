import { randomUUID } from 'node:crypto';
import { connect, JSONCodec } from 'nats';
import pino from 'pino';

interface NatsResponse {
  requestId: string;
  result?: string;
  error?: string;
}

const logger = pino({
  level: 'info',
  transport: {
    target: 'pino-pretty',
  },
});
const NATS_SERVER = 'nats://localhost:4222';
const nc = await connect({ servers: NATS_SERVER });
logger.info(`Connected to NATS server at ${NATS_SERVER}`);

const jc = JSONCodec();

async function sendRequest() {
  const requestId = randomUUID();

  const data = {
    requestId,
    num1: 0.1,
    num2: 0.2,
  };

  try {
    logger.info({ requestId, data }, 'Sending RPC request to add numbers');

    const msg = await nc.request('rpc.add', jc.encode(data), {
      timeout: 20_000,
    });

    const result = jc.decode(msg.data) as NatsResponse;
    if (result.error) {
      logger.error({ requestId, error: result.error }, 'Error in response');
    } else {
      logger.info({ requestId, result }, 'Received successful response');
    }
  } catch (error) {
    logger.error({ err: error, requestId }, 'Failed to get a response:');
  }
}

setInterval(sendRequest, 5000);

process.on('SIGINT', async () => {
  logger.info('Closing NATS connection...');
  await nc.close();
  process.exit();
});
