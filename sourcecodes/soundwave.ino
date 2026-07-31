#define TRIG 9
#define ECHO 8

void setup() {
  Serial.begin(9600);  // 9600의 속도로 시리얼 통신. 속도와 안정성 반비례

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  long duration, distance;

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);   // 물체에 반사되어 돌아온 초음파의 시간
  distance = duration * 17 / 1000;  // cm 단위 변환 공식

  Serial.println(distance);
  

  delay(1000);
}
