package br.com.fiap;

import java.util.Scanner;
 
public class TesteFolhaDePagamentoScanner {
	
	public static void main(String[] args) {
		FolhaDePagamento folha = new FolhaDePagamento();
		double salarioBruto, descontoINSS, valorPlanoDeSaude, salarioLiquido;
		int numeroDeDependentes; //variaveis
		Scanner scan;
		
		try {
			scan = new Scanner(System.in);
			//lendo informações difitadas pelo usuário
			System.out.println("Valor do salário bruto: ");
			salarioBruto = scan.nextDouble(); //metodo q me retorna um double
			System.out.println("Digite número de dependentes: ");
			numeroDeDependentes = scan.nextInt();
			System.out.println("Digite desconto de INSS: ");
			descontoINSS = scan.nextDouble();
			System.out.println("Digite valor do plano de saúde");
			valorPlanoDeSaude = scan.nextDouble();
			
			//atribuindo os valores ao objeto de classe
			folha.salarioBruto = salarioBruto;
			folha.numeroDeDependentes = numeroDeDependentes;
			folha.descontoINSS = descontoINSS;
			folha.valorPlanoDeSaude = valorPlanoDeSaude;
			
			salarioLiquido = folha.calcularSalarioLiquido();
			
			// exibir os valores e resultado
			System.out.println("Exibindo as informações:" +
			"\nSalário bruto:" + folha.salarioBruto + folha.salarioBruto
			+ "\nDesconto INSS: " + folha.descontoINSS + "%" +
			"\nPlano de Saúde:" + folha.valorPlanoDeSaude +
			"\nSalário Líquido: " + salarioLiquido);
		} catch (Exception e) {
			System.out.println("Formato incorreto!");
		}
		
		
		
		

	}

}
