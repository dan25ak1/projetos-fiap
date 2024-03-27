package br.com.fiap;

import javax.swing.JOptionPane;

public class MédiaAritmética {
	public static void main(String[] args) {
		double num1 = 0, num2 = 0, num3 = 0, num4 = 0;
		String aux;
		try {
		aux = JOptionPane.showInputDialog("Digite a nota da prova 1: ");
		num1 = Integer.parseInt(aux);
		aux = JOptionPane.showInputDialog("Digite a nota da prova 2: ");
		num2 = Integer.parseInt(aux);
		aux = JOptionPane.showInputDialog("Digite a nota da prova 3: ");
		num3 = Integer.parseInt(aux);
		aux = JOptionPane.showInputDialog("Digite a nota da prova 4: ");
		num4 = Integer.parseInt(aux);
			JOptionPane.showConfirmDialog(null, "\nMédia dos valores = " + (num1 + num2 + num3 + num4)/4);
		
		} catch (Exception e) {
			JOptionPane.showConfirmDialog(null, "Formato de entrada incorreto: ");
		}
	
		
	}

}
