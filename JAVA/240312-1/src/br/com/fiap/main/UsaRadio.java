package br.com.fiap.main;

import br.com.fiap.bean.Radio;

public class UsaRadio {
    public static void main(String[] args) {
        Radio radio1 = new Radio();

        radio1.estacao = 89.1f;
        radio1.volume = 5;
        radio1.aumentarVolume();
        radio1.aumentarVolume();
        radio1.trocarEstacao(101.2f);
        radio1.mostrar();
    }
}
