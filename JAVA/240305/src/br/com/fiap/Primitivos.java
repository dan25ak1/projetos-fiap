package br.com.fiap;

public class Primitivos {
	
	public static void main(String[] args) {
		//declaração de variável
		char sexo;
		//inicializando a variável (atribuindo valores)
		sexo = 'F';
		//declaração e inicialização de variavel
		byte idade = 25;
		short codigo = 15650;
		int alunos = 50, turmas = 11;
		long brasileiros =216635748;
		float media = 8.7f; 
		double cotacaoDoDolar = 4.95;
		boolean alternativa = false; // true
		
		
		System.out.println("\\Sexo:" + sexo + "\nIdade:" + idade);
		System.out.println("Código:" + codigo + " Alunos:" + alunos + " Turmas:" + turmas);
		System.out.println("'Habitantes':" + brasileiros + "Média:" + media);
		System.out.println("Cotação do \"dólar\" US$:" + cotacaoDoDolar);
		System.out.println("Alternativa:" + alternativa);
	}
}
