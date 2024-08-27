package br.com.fiap;

public class TesteRadioEncapsulada {

	public static void main(String[] args) {
		RadioEncapsulada radio1 = new RadioEncapsulada();
		radio1.setEstacao(89.1f);
		radio1.setVolume(5);
		radio1.aumentarVolume();
		radio1.aumentarVolume();
		radio1.setEstacao(92.5f);
		radio1.mostrar();
		
	}

}
