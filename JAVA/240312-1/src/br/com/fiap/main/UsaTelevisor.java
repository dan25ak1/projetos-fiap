package br.com.fiap.main;

import br.com.fiap.bean.Televisor;

public class UsaTelevisor {
    public static void main(String[] args) {
        Televisor tv = new Televisor();

        tv.canal = 95f;
        tv.volume = 24;
        tv.aumentarVolume();
        tv.aumentarVolume();
        tv.trocarCanal(96f);
        tv.mostrar();
    }
}
