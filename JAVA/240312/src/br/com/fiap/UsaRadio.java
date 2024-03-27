package br.com.fiap;

public class UsaRadio {
	
	public static void main(String[] args) {
		//declarar um obj da classe
		//Radio radio1;
		//instanciar um obj da classe
		Radio radio1 = new Radio();
		
		radio1.volume = 5;
		radio1.estacao = 89.1f;
		radio1.mostrar();
		
		radio1.trocarEstacao(92.5f);
		radio1.aumentarVolume();
		radio1.aumentarVolume();
		radio1.mostrar();
		
	}

}
