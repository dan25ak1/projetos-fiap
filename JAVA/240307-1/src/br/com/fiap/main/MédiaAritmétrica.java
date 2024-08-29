package br.com.fiap.main;

import javax.swing.*;

public class MédiaAritmétrica {
    public static void main(String[] args) {
        int num1, num2, num3, num4;
        String aux;
        try{
            aux = JOptionPane.showInputDialog("Digite o primeiro número:");
            num1 = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o segundo número:");
            num2 = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o terceiro número:");
            num3 = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o quarto número:");
            num4 = Integer.parseInt(aux);
            JOptionPane.showMessageDialog(null,"Média dos quatro número: " + (num1 + num2 + num3 + num4)/2 );
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de número incorreto!");
        }
    }
}
