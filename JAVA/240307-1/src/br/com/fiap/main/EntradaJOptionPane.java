package br.com.fiap.main;

import javax.swing.*;
import java.awt.*;

public class EntradaJOptionPane {
    public static void main(String[] args) {
        int num1 = 0, num2 = 0;
        String aux;
        try{
            aux = JOptionPane.showInputDialog("Digite um número");
            num1 = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite outro número");
            num2 = Integer.parseInt(aux);
            JOptionPane.showMessageDialog(null, "Valor 1: " + num1 + "\nValor 2: " + num2 + "\nSoma dos Valores = " + (num1 + num2));
        } catch (HeadlessException e) {
            JOptionPane.showMessageDialog(null, "Formato de número incorreto");
        }
    }
}
