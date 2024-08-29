package br.com.fiap.main;

import javax.swing.*;

public class SuaIdade {
    public static void main(String[] args) {
        int anoAtual, anoNasc;
        String aux;
        try {
        aux = JOptionPane.showInputDialog("Digite o ano atual:");
        anoAtual = Integer.parseInt(aux);
        aux = JOptionPane.showInputDialog("Digite seu ano de nascimento");
        anoNasc = Integer.parseInt(aux);
        JOptionPane.showMessageDialog(null, "Você tem " + (anoAtual - anoNasc) + " anos");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de número incorreto");
        }
    }
}
