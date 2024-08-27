package br.com.fiap;

import java.time.LocalDate;
import java.util.Scanner;

public class UsaPessoa2 {

	public static void main(String[] args) {
		
		LocalDate dataAtual = LocalDate.now();
		int anoAtual = dataAtual.getYear();
		Pessoa p1;                  //jogando valores em variaveis
		Scanner scan;
		//String nome;
		//int anoNascimento;
		try {
			scan = new Scanner(System.in);
			System.out.println("Digite seu nome e ano de nascimento");
			//nome = scan.nextLine(); //para ler espaço entre nome e sobrenome tambem
			//anoNascimento = scan.nextInt();
			
			//p1 = new Pessoa(nome, anoNascimento);
			p1 = new Pessoa(scan.next(), scan.nextInt());
			int idade = p1.calculaIdade(anoAtual);
			
			System.out.println("Nome: " + p1.getNome());
			System.out.println("Idade: " + idade + " anos");
		} catch (Exception e) {
			System.out.println("Nome ou Ano Nascimento inválido(s)!");
			
		}

	}

}
