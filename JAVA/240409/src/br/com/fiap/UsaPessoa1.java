package br.com.fiap;

import java.time.LocalDate;

public class UsaPessoa1 {

	public static void main(String[] args) {
		LocalDate dataAtual = LocalDate.now();
		int anoAtual = dataAtual.getYear();
		
		Pessoa p1 = new Pessoa();
		p1.setNome("Astrogildo");
		p1.setAnoNascimento(1999);
		int idade = p1.calculaIdade(anoAtual);

		Pessoa p2 = new Pessoa("Berisvaldo", 1880);
		
		System.out.println("Nome: " + p1.getNome());
		System.out.println("Idade: " + idade + " anos");
		System.out.println("Nome: " + p2.getNome());
		System.out.println("Idade: " + p2.calculaIdade(anoAtual) + " anos");


	}

}
