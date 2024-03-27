package br.com.fiap;

import java.util.Scanner;

public class Idade {
	public static void main(String[] args) {
		int ano = 0;
		Scanner scan; 
		scan = new Scanner(System.in);
		System.out.println("Digite o ano que você nasceu: ");
		ano = scan.nextInt();
		System.out.println("Em 2024 você tem/terá: " + (2024 - ano) + " Anos");
		
		
		
		
	}

}
