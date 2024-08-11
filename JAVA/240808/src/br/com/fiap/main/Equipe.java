package br.com.fiap.main;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;

public class Equipe {
    private String nome;
    private ArrayList<String> integrantes;

    public Equipe() {
    }

    public Equipe(String nome, ArrayList<String> integrantes) {
        this.nome = nome;
        this.integrantes = integrantes;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public ArrayList<String> getIntegrantes() {
        return integrantes;
    }

    public void setIntegrantes(ArrayList<String> integrantes) {
        this.integrantes = integrantes;
    }

    public void listaEQuipe() {
        String exibe = "Nome da Equipe: " + nome;
        Collections.sort(integrantes);
        int cont = 1;
        for (String i : integrantes) {
            exibe += "\nIntegrante " + cont + ": " + i;
            cont++;
        }
        JOptionPane.showMessageDialog(null,exibe);
    }
}
