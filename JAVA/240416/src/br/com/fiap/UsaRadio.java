package br.com.fiap;

import javax.swing.JOptionPane;

public class UsaRadio {

	public static void main(String[] args) {
		Radio radio1;
		String aux;
		float estacao;
		int volume, escolha;
		try {
			aux = JOptionPane.showInputDialog("Escolha o volume"); //(jop CTRL + ESPACE)
			volume = Integer.parseInt(aux);
			aux = JOptionPane.showInputDialog("Escolha a estação");
			estacao = Float.parseFloat(aux);
			
			radio1 = new Radio(volume, estacao);
			 
			JOptionPane.showMessageDialog(null, "Estação: " + radio1.getEstacao() + "\nVolume: " + radio1.getVolume());
			
			aux = JOptionPane.showInputDialog("Escolha uma opção: " + "\n(1) Aumentar volume" +
							"\n(2) DIminuir volume" + "\n(3) Trocar de estação");
			escolha = Integer.parseInt(aux);
			
			switch (escolha) {
			case 1:
				radio1.aumentarVolume();
				break;
			case 2:
				radio1.diminuirVolume();
				break;
			case 3:
				aux = JOptionPane.showInputDialog("Escolha a estação");
				estacao = Float.parseFloat(aux);
				radio1.setEstacao(estacao);
				break;

			default:
				throw new Exception("Opção inválida (1-3)");
				}
				
			JOptionPane.showMessageDialog(null, "Estação: " + radio1.getEstacao() + "\nVolume: " + radio1.getVolume());
	
		} catch (Exception e) {
			System.out.println("Erro: " + e.getMessage());
		}

	}

}
