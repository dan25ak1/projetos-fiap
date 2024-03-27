package br.com.fiap;

import java.util.Scanner;

public class CalcularPi {
	static double raio = 0;
	static double pi = 3.14f;
	public static void main(String[] args) {
		Scanner scan;
		scan = new Scanner (System.in);
		System.out.println("Diga o valor do raio de um círculo: ");
		raio = scan.nextInt();
		System.out.println("O área do círculo é: " + (pi * (raio * raio)));
		
}
}
