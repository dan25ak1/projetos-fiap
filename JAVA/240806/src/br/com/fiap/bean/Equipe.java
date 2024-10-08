package br.com.fiap.bean;

import javax.swing.*;

public class Equipe {
    private String nome;
    private String[] integrantes;

    public Equipe() {
    }
    public Equipe(String nome, String[] integrantes) {
        this.nome = nome;
        this.integrantes = integrantes;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String[] getIntegrantes() {
        return integrantes;
    }
    public void setIntegrantes(String[] integrantes) {
        this.integrantes = integrantes;
    }
    public void listaEquipe() {
        String exibe = "Nome da equipe: " + nome + "\n";
        int cont = 1;
        for (String i : integrantes) {
            exibe += "Integrante " + cont + ": " + i + "\n";
            cont++;
        }
        JOptionPane.showMessageDialog(null, exibe);
    }
}
