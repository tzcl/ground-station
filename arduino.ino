// Store alt/az data from Raspberry Pi
float alt = 0.0;
float azi = 0.0;
const byte BUFFER_LEN = 32;
char buff[BUFFER_LEN];        // used in recvData
char parseBuffer[BUFFER_LEN]; // used in parseData
bool newData = false;

void setup() { Serial.begin(9600); }

void loop() {
  // Parse altitude/azimuth
  recvData();
  if (newData) {
    strcpy(parseBuffer,
           buff); // necessary becuase strtok replaces parsed data with \0
    parseData();
    printData();
    newData = false; // reset
  }
}

void recvData() {
static boolean receiving = false;
 static byte index = 0;
 char startMarker = 's';
 char endMarker = '\n';
 char dataChar;

 while (Serial.available() > 0 && newData == false) {
   dataChar = Serial.read();

   if (receiving) {
     if (dataChar != endMarker) {
       buff[index] = dataChar;
       index++;
       if (index >= BUFFER_LEN) {
         index = BUFFER_LEN - 1;
       }
     } else {
       buff[index] = '\0';
       receiving = false;
       index = 0;
       newData = true;
     }
   }
   ​ else if (dataChar == startMarker) {
     receiving = true;
   }
 }
}
void parseData() {
  char *stkIndex;
  // Obtain first number and convert to float
  stkIndex = strtok(parseBuffer, ",");
  alt = atof(stkIndex);
  // Obtain second number and convert to float
  stkIndex = strtok(NULL, ",");
  azi = atof(stkIndex);
}

void printData() {
  Serial.print("Received: ");
  Serial.print(alt, 10); // display 10 decimal places, tho any significant
                         // figure beyond the original data is made up
  Serial.print(", ");
  Serial.print(azi, 10); // display 10 decimal places
  Serial.println();
}
