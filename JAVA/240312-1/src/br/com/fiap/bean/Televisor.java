package br.com.fiap.bean;

public class Televisor {
    public int volume;
    public float canal;

    public void aumentarVolume() {
        volume++;
    }
    public void diminuirVolume() {
        volume--;
    }
    public void trocarCanal(float c) {
        canal = c;
    }
    public void mostrar() {
        System.out.println("Volume " + volume + "\nCanal: " + canal);
    }
}

