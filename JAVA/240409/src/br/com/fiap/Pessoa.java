package br.com.fiap;

import java.time.LocalDate;

public class Pessoa {
	//atributos encapsulados
	private String nome;
	private int anoNascimento;
	//construtores
	//construtor vazio
	public Pessoa() { //(CRTL + 3 -> gcfs)
		
	}
	// construtor com passagem de parâmetros
	public Pessoa(String nome, int anoNascimento) { //(CRTL + 3 -> gcuf)
		this.nome = nome;
		this.anoNascimento = anoNascimento;
	}
	// métodos getters & setters (CRTL+3 -> ggas)
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public int getAnoNascimento() {
		return anoNascimento;
	}
	public void setAnoNascimento(int anoNascimento) {
		try {
			this.anoNascimento = anoNascimento;
			LocalDate dataAtual = LocalDate.now();
			int anoAtual = dataAtual.getYear();
			if (anoNascimento >= 1900 && anoNascimento <= anoAtual) {
				this.anoNascimento = anoNascimento;		
			} else {
				throw new Exception("Valor inválido! (1900-Ano Atual)");
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	// métodos da classe
	public int calculaIdade(int anoAtual) {
		return anoAtual - anoNascimento;
	}
	
	
}
