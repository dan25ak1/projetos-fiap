package br.com.fiap;

public class RadioUsar {

	public static void main(String[] args) {
		Radio radio1 = new Radio();
		
		radio1.estacao = 89.1f;
		radio1.volume = 5;
		radio1.aumentarVolume();
		radio1.aumentarVolume();
		radio1.trocarEstacao(92.5f);
		radio1.mostrar();

	}

}
