package br.com.fiap.bean;

public class ArCondicionado {
    public int temp;
    public String modo;

    public void aumentarTemperatura() {
        temp++;
    }
    public void diminuirTemperatura() {
        temp--;
    }
    public void trocarModo(String m) {
        modo = m;
    }
    public void mostrar() {
        System.out.println("Temperatura: " + temp + "\nModo: " + modo);
    }
}