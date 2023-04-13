import mqtt from './mqtt';

mqtt.listen(1883, function () {
  console.log('server started and listening on port ', 1883);
});
