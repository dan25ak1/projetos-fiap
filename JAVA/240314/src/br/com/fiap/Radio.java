package br.com.fiap;

public class Radio {
	
	public int volume;
	public float estacao;
	
	public void aumentarVolume() {
		volume++;
	}
	public void diminuirVolume() {
		volume--;
	}
	public void trocarEstacao(float e) {
		estacao = e;
	}
	public void mostrar() {
		System.out.println("Volume: " + volume + "\nEstação: " +
	estacao);
	}
}
