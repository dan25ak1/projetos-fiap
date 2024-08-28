package br.com.fiap;

public class TelevisorEncapsulado {
	//atributos
	private int volume;
	private int canal;
	
	// métodos getters/setters (crtl+3 -> ggas
	public int getVolume() {
		return volume;
	}
	public void setVolume(int volume) {
		try {
			if (volume >= 0 && volume <= 20) {
				this.volume = volume;
			}
			else {
				throw new Exception("Volume fora da faixa pertimitda (0-20)");
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	public int getCanal() {
		return canal;
	}
	public void setCanal(int canal) {
		try {
		    if (canal == 2 || canal == 4 || canal == 7 || canal == 13) {
				this.canal = canal;
			}
			else {
				this.canal = 2;
				throw new Exception("canal incorreto. Canais pertimitidos (2-4-7-13)");
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		 
	}
	
	//métpdps particulares
	public void aumentarVolume( ) {
		if (volume < 20) {
			volume++;
		}
	}
	public void diminuir() {
		if (volume > 0) {
			volume--;
		}
	}
	
	public void mostrar() {
		System.out.println("Canal: " + getCanal() + "\nVolume: " + getVolume());
	}
		
	
}
