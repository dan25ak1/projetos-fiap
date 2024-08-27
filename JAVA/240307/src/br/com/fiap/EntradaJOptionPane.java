package br.com.fiap;

import javax.swing.JOptionPane;

public class EntradaJOptionPane {

	public static void main(String[] args) {
		int num1 = 0, num2 = 0;
		String aux;
		try {
			aux = JOptionPane.showInputDialog("Digite um número");
			num1 = Integer.parseInt(aux);
			aux = JOptionPane.showInputDialog("Digite outro número");
			num2 = Integer.parseInt(aux);
			JOptionPane.showConfirmDialog(null,
					"Valor 1: " + num1 + "\nvalor 2: " + num2 +
					"\nsoma dos valores = " + (num1 + num2));
		} catch (Exception e) {
			JOptionPane.showConfirmDialog(null,"Formato de número incorreto");
			
		}

	}

}
