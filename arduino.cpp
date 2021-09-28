// Store alt/az data from Raspberry Pi
float altitude = 0.0;
float azimuth = 0.0;

const byte BUFFER_LEN = 32;
char buffer[BUFFER_LEN];
bool newData = false;

void setup() {
  // Set up the serial connection
  Serial.begin(9600);
  Serial.println("Arduino is ready");

  // Other setup code
  // ...
}

void loop() {
  // Parse altitude/azimuth
  recvData();
  printData(); // send received data back to the Pi for testing

  // Other loop code
  // ...
}

void recvData() {
  static boolean receiving = true;
  static byte index = 0;
  char endMarker = '\n';
  char data;

  while (Serial.available() > 0 && !newData) {
    data = Serial.read();

    if (receiving) {
      if (data != endMarker) {
        buffer[index++] = data;
        if (index >= BUFFER_LEN) {
          index = BUFFER_LEN - 1;
        }
      } else {
        data[index] = '\0';
        receiving = false;
        index = 0;
        newData = true;
      }
    }
  }

  if (newData) {
    parseData();
    newData = false;
  }
}

void parseData() {
  char *index;
  char tmp[BUFFER_LEN];
  strcpy(tmp, buffer);

  index = strtok(tmp, ",");
  altitude = atof(index);

  index = strtok(NULL, ",");
  azimuth = atof(index);
}

void printData() {
  Serial.print("Received: ");
  Serial.print(altitude);
  Serial.print(", ");
  Serial.print(azimuth);
  Serial.println();
}
