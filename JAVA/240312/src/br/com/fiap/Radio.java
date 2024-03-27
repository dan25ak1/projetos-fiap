package br.com.fiap;

public class Radio {

	//atributos
	public int volume;
	public float estacao;
	
	//metodos
	public void aumentarVolume() {
		volume++;
	}
	public void diminuirVolume() {
		volume--;	
	}
	public void trocarEstacao(float station) {
		estacao = station;
		
	}
	public void mostrar() {
		System.out.println("Volume: "+ volume + "\nEstação: " + estacao);
	}
	
}