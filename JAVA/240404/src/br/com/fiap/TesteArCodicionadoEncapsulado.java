package br.com.fiap;

import java.util.Scanner;

public class TesteArCodicionadoEncapsulado {

	public static void main(String[] args) {
		ArcondicionadoEncapsulado ac = new ArcondicionadoEncapsulado();
		Scanner scan;
		int escolha = 0;
		try {
			scan = new Scanner(System.in);
			System.out.println("Escolha um modo");
			ac.setModo(scan.next());
			System.out.println("Escolha uma temperatura");
			ac.setTemperatura(scan.nextInt());
			System.out.println("Faça sua escolha:" + "\n(1) Muda modo" + "\n(2) Aumenta temperatura" + 
			"\n(3) Diminuir temperatura");
			if (escolha == 1) {
				System.out.println("Escolha um novo modo");
				ac.trocarModo(scan.next());
			} else if (escolha == 2){
				ac.aumentarTemperatura();
			} else if (escolha == 3){
				ac.DiminuirTemperatura();
			} else {
				System.out.println("Escolha inválida (15-26)");
				
		} catch (Exception e) {
		System.out.println("Formato incorreto");
		}
	}

}
