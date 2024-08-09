package br.com.fiap.main;

import javax.swing.*;
import java.util.ArrayList;

public class UsaEquipe {
    public static void main(String[] args) {
        Equipe grupo;
        String nome, membro;
        ArrayList<String> integrantes = new ArrayList<String>();
        do {
            try {
                nome = JOptionPane.showInputDialog("Digite o nome da equipe");
                do {
                    membro = JOptionPane.showInputDialog("Digite o integrante desta equipe ou digite \"fim\" para encerrar");
                    integrantes.add(membro);
                } while (!membro.equalsIgnoreCase("fim"));
                //integrantes.remove(integrantes.size() - 1);
                integrantes.removeLast();
                grupo = new Equipe(nome, integrantes);
                grupo.listaEQuipe();
                integrantes.clear();

            } catch (Exception e) {
                JOptionPane.showMessageDialog(null,e.getMessage());
            }
        } while (JOptionPane.showConfirmDialog(null, "Deseja continuar?", "Atenção", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);
        JOptionPane.showMessageDialog(null,"Fim de Programa");
    }
}
