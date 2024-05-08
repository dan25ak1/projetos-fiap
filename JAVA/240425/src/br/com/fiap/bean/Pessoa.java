package br.com.fiap.bean;

import java.time.LocalDate;
import java.time.Period;

import javax.swing.JOptionPane;

public class Pessoa {
 // atributos
	private String nome;
	private LocalDate dataNascimento;
	//construtores
	public Pessoa() {
	}
	public Pessoa(String nome, LocalDate dataNascimento) {
		this.nome = nome;
		setDataNascimento(dataNascimento);
	}
	// métodos getters & setters
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public LocalDate getDataNascimento() {
		return dataNascimento;
	}
	public void setDataNascimento(LocalDate dataNascimento) {
		try {
			LocalDate inicio = LocalDate.parse("1899-12-31"); //parse serve para jogar uma data para LocalDate (um dia antes do solicitado)
			LocalDate fim = LocalDate.now().plusDays(1); //adicionar um 1
			if (dataNascimento.isAfter(inicio) && dataNascimento.isBefore(fim)) {
				this.dataNascimento = dataNascimento;
			} else {
				throw new Exception("Data fora da faixa permitida");
			}
		} catch (Exception e) {
			JOptionPane.showMessageDialog(null, e.getMessage());
			System.exit(0); // encerra programa após o erro
		}
	}
	//métodos da classe
	public int calculaIdade() {
		LocalDate dataAtual = LocalDate.now();
		Period idade = Period.between(dataNascimento, dataAtual);
		return idade.getYears();
	}
}
