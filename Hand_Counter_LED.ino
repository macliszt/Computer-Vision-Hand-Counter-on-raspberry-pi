int red = 5;
int blue = 6;
int green = 7;
int yellow = 8;
int white = 9;


void setup() {
  Serial.begin(9600);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(white,OUTPUT);
  pinMode(yellow,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming message from Raspberry Pi
    String message = Serial.readStringUntil('\n');
    message.trim();  // Remove any leading/trailing spaces

    // Check if the message is "Face Recognized"
    if (message == "red") {
      digitalWrite(red, HIGH);  // Turn on LED (access granted)
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW); 
      digitalWrite(yellow, LOW);
      digitalWrite(white, LOW);
    } 
    // Check if the message is "Face Not Recognized"
    else if (message == "blue") {
      digitalWrite(blue, HIGH);  // Turn off LED (access denied)
      digitalWrite(red, LOW);
      digitalWrite(green, LOW); 
      digitalWrite(yellow, LOW);
      digitalWrite(white, LOW);
    }
    // Check if the message is "No Face Detected"
    else if (message == "green") {
      digitalWrite(green, HIGH);  // Turn off LED (no face detected)
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(yellow, LOW);
      digitalWrite(white, LOW);
    }
    else if (message == "yellow") {
      digitalWrite(yellow, HIGH);  // Turn on LED (access granted)
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW); 
      digitalWrite(white, LOW);
    }
    else if (message == "white") {
      digitalWrite(white, HIGH);  // Turn off LED (access denied)
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW); 
      digitalWrite(yellow, LOW);
      
    }
    else if(message == "none"){
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW); 
      digitalWrite(yellow, LOW);
      digitalWrite(white, LOW);
    }
  }
}
