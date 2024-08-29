package br.com.fiap.main;

import br.com.fiap.bean.ArCondicionado;

public class UsarArCondicionado {
    public static void main(String[] args) {
        ArCondicionado ac = new ArCondicionado();

        ac.temp = 19;
        ac.modo = "Modo silêcioso";
        ac.trocarModo("Ventilação");
        ac.mostrar();
    }
}
