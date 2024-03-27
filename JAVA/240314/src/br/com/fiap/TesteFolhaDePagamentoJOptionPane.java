package br.com.fiap;

import javax.swing.JOptionPane;

public class TesteFolhaDePagamentoJOptionPane {
	public static void main(String[] args) {
		FolhaDePagamento folha = new FolhaDePagamento();
		double salarioBruto, descontoINSS, valorPlanoDeSaude, salarioLiquido;
		int numeroDeDependentes; //variaveis
		String aux;
		try {
			//lendo informações digitadas pelo usuário
			aux= JOptionPane.showInputDialog("Valor do salário bruto: ");
			salarioBruto = Double.parseDouble(aux);
			aux = JOptionPane.showInputDialog("Digite número de dependentes: ");
			numeroDeDependentes = Integer.parseInt(aux);
			aux = JOptionPane.showInputDialog("Digite desconto de INSS: ");
			descontoINSS = Double.parseDouble(aux);
			aux = JOptionPane.showInputDialog("Digite valor do plano de saúde");
			valorPlanoDeSaude = Double.parseDouble(aux);
			
			//atribuindo os valores ao objeto da classe
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
			JOptionPane.showMessageDialog(null, "Formato incorreto!");
		}
	}
}
		
	

