package br.com.fiap;

public class Radio {
	//atributos encapsulados
	private int volume;
	private float estacao;
	//construtorees (CTRL + 3: vazio -> gcfs | parâmetros -> gcuf)
	public Radio() {
	}
	public Radio(int volume, float estacao) {
		setVolume(volume);
		setEstacao(estacao);
	}
	//metodos getters & setters (CRTL + 3: ggas)
	public int getVolume() {
		return volume;
	}
	public void setVolume(int volume) {
		try {
			if (volume >= 0 && volume <= 10) {
				this.volume = volume;
			} else {
				throw new Exception("Volume fora da faixa permitida (0-10)");
			}
		} catch (Exception e) {
			System.out.println("Erro: " + e.getMessage());
		}
	}
	public float getEstacao() {
		return estacao;
	}
	public void setEstacao(float estacao) {
		try {
			if (estacao >= 80.0 && estacao <= 105.0f) {
				this.estacao = estacao;
			} else {
				this.estacao = 80.0f;
				throw new Exception("Estação fora de sintonia (80-105.0)");
			}
		} catch (Exception e) {
			System.out.println("Erro: " + e.getMessage());
		}
	}
	// métodos da classe
	public void aumentarVolume() {
		if (volume < 10) {
			volume++;
		}
	}
	public void diminuirVolume() {
		if (volume > 0) {
			volume--;
		}
	}
	
}
