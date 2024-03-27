package br.com.fiap;

public class UsarArCondicionado {

	public static void main(String[] args) {
	
		ArCondicionado ac = new ArCondicionado();
		ac.temperatura = 23;
		ac.modo = "Resfriar";
		ac.mostrar();
		ac.trocarModo("Ventilar");
		ac.mostrar();
	}

}
