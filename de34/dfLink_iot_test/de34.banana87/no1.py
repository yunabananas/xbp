import processing.serial.*;
Serial myPort;

void setup() {
  myPort = new Serial(this, "dev/tty.usbserial-110", 9600);//実際に繋がったポート番号で
}

void draw() {
	if(myPort.read()=='A'){//「A」が送られて来たら
		launch("C:\abc.mpg");//動画を再生。（関連付けられたプレイヤーで再生）
	}
}