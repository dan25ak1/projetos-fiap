package br.com.fiap;

public class UsarTelevisor {
	
	public static void main(String[] args) {
	
		Televisor tv = new Televisor();
		tv.volume = 10;
		tv.canal = 5;
		tv.mostrar();
		tv.diminuirVolume();
		tv.trocarCanal(9);
		tv.mostrar();
}
}
