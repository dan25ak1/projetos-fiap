package br.com.fiap.bean;

public class Quadrado {
	//atributo
	private float lado;
	//construtor vazio
	public Quadrado() {}
	//construtor com parâmetro
	public Quadrado(float lado) {
		this.lado = lado;
	}
	// métodos getters and setters
	public float getLado() {
		return lado;
	}
	public void setLado(float lado) {
		this.lado = lado;
	}
	public float calcularArea() {
		return getLado() * getLado();
	}
}
