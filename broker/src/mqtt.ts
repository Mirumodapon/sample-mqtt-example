import Aedes from 'aedes';
import { createServer } from 'net';

const mqttBroker = new Aedes();
const server = createServer(mqttBroker.handle);

mqttBroker.on('client', function (client) {
  console.log(`Client Connected: ${client.id}`);
});

mqttBroker.on('publish', function (packet, client) {
  if (client) console.log(`Message: ${packet.payload}`);
});

mqttBroker.on('subscribe', function (subscriptions, _) {
  console.log(`Subscribe: ${subscriptions.map((s) => s.topic).join(',')}`);
});

export default server;

const sendTestPacket = () => {
  mqttBroker.publish(
    {
      cmd: 'publish',
      qos: 0,
      dup: false,
      retain: false,
      topic: 'TEST',
      payload: 'This is the test payload.'
    },
    function (err) {
      if (err) console.log(err);
    }
  );

  console.log('Sent the message.');

  return;
};

setInterval(sendTestPacket, 5000);
