package br.com.fiap;

import java.util.Scanner;

public class UsaTelevisorEncapsulada {

	public static void main(String[] args) {
		
		TelevisorEncapsulado tv = new TelevisorEncapsulado();
//		tv.setVolume(10);
//		tv.setCanal(5);
//		tv.mostrar();
		
		int escolha = 0;
		Scanner scan;
		try {
			scan = new Scanner(System.in);
			System.out.println("Escolha um canal e seu volume");
			tv.setCanal(scan.nextInt());
			tv.setVolume(scan.nextInt());
			System.out.println("Faça sua escolha: " + "\n(1) Mudar canal" + "\n(2) Mudar volume" + "\n(3) Aumentar volume" + "\n(4) Diminuir volume");
			escolha = scan.nextInt();
			if (escolha == 1) {
				System.out.println("Escolha novo canal");
				tv.setCanal(scan.nextInt());
			} else if (escolha == 2 ) {
				System.out.println("Escolha novo Volume");
				tv.setVolume(scan.nextInt());
			} else if (escolha == 3) {
				System.out.println("Aumentando Volume...");
				tv.setVolume(scan.nextInt());
			} else if (escolha == 4) {
				System.out.println("Aumentando Volume...");
				tv.setVolume(scan.nextInt());
			} else {
				System.out.println("Escolha incorreta! (1-4");
			}
			tv.mostrar();
		} catch (Exception e) {
			System.out.println("Formato incorreto!");
		}
		
		
		
	}

}
