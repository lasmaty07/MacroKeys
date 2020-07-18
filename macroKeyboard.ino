//Macro Keyboard using Arduino Micro.
//Lmjd14 17/05/2020
//This code is free to use with attribution

//#include <Keyboard.h>

const int A = 2;
const int S = 4;
const int D = 6;
const int F = 8;
const int Q = 3;
const int W = 5;
const int E = 7;
const int R = 9;
const int P = 1;

bool a = false;
bool s = false;
bool d = false;
bool f = false;
bool q = false;
bool w = false;
bool e = false;
bool r = false;

int val = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //Setup buttons
  pinMode(A, INPUT_PULLUP);
  pinMode(S, INPUT_PULLUP);
  pinMode(D, INPUT_PULLUP);
  pinMode(F, INPUT_PULLUP);
  pinMode(Q, INPUT_PULLUP);
  pinMode(W, INPUT_PULLUP);
  pinMode(E, INPUT_PULLUP);
  pinMode(R, INPUT_PULLUP);
  pinMode(P, INPUT);

}

void loop() {

  if (digitalRead(A) == LOW) { 
    a = true;
  } else {
    a = false;
  }

  if (digitalRead(S) == LOW) { 
    s = true;
  } else {
    s = false;
  }
  if (digitalRead(D) == LOW) { 
    d = true;
  } else {
    d = false;
  }
  if (digitalRead(F) == LOW) { 
    f = true;
  } else {
    f = false;
  }
  if (digitalRead(Q) == LOW) { 
    q = true;
  } else {
    q = false;
  }
  if (digitalRead(W) == LOW) { 
    w = true;
  } else {
    w = false;
  }
  if (digitalRead(E) == LOW) { 
    e = true;
  } else {
    e = false;
  }
  if (digitalRead(R) == LOW) { 
    r = true;
  } else {
    r = false;
  }

    val = analogRead(P);
    val = map(val, 0, 1023, 0, 1000);

    Serial.print(a);Serial.print("|");
    Serial.print(s);Serial.print("|");
    Serial.print(d);Serial.print("|");
    Serial.print(f);Serial.print("|");
    Serial.print(q);Serial.print("|");
    Serial.print(w);Serial.print("|");
    Serial.print(e);Serial.print("|");
    Serial.print(r);Serial.print("|");
    Serial.println(val);
  delay(150);
}
