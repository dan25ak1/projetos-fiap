package br.com.fiap.view;

import br.com.fiap.controller.FilmeController;

import javax.swing.*;
import java.util.Scanner;

public class FilmeView {

    public static void main(String[] args) {

        String titulo, genero, produtora;
        String[] escolha = {"Inserir", "Alterar", "Excluir", "Listar Todos", "Listar Um"};
        int codigo, opcao;

        FilmeController filmeController = new FilmeController();
        Scanner leitura = new Scanner(System.in);

        do {

            try {

                opcao = JOptionPane.showOptionDialog(null, "Escolha uma das opções abaixo para manipular um Filme", "Escolha", JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, escolha, escolha[0]);

                switch (opcao) {

                    case 0:

                        System.out.println("\nDigite o código do filme");
                        codigo = leitura.nextInt(); leitura.nextLine();

                        System.out.println("\nDigite o titulo do filme");
                        titulo = leitura.nextLine();

                        System.out.println("\nDigite o gênero do filme");
                        genero = leitura.nextLine();

                        System.out.println("\nDigite a produtora do filme");
                        produtora = leitura.nextLine();

                        System.out.println(filmeController.inserirFilme(codigo, titulo, genero, produtora));
                        break;

                    case 1:

                        System.out.println("\nDigite o código do filme");
                        codigo = leitura.nextInt(); leitura.nextLine();

                        System.out.println("\nDigite o NOVO titulo do filme");
                        titulo = leitura.nextLine();

                        System.out.println("\nDigite o NOVO gênero do filme");
                        genero = leitura.nextLine();

                        System.out.println("\nDigite a NOVA produtora do filme");
                        produtora = leitura.nextLine();

                        System.out.println(filmeController.alterarFilme(codigo, titulo, genero, produtora));
                        break;

                    case 2:

                        System.out.println("\nDigite o código do filme");
                        codigo = leitura.nextInt(); leitura.nextLine();

                        System.out.println(filmeController.excluirFilme(codigo));
                        break;

                    case 3:

                        JOptionPane.showMessageDialog(null, filmeController.listarTodos());
                        break;

                    case 4:

                        System.out.println("\nDigite o código do filme");
                        codigo = leitura.nextInt(); leitura.nextLine();

                        JOptionPane.showMessageDialog(null, filmeController.listarUmFilme(codigo));
                        break;

                    default:

                        System.out.println("Opção inválida!");

                }

            } catch (Exception e) {

                System.out.println("Erro: " + e.getMessage());;

            }

        } while (JOptionPane.showConfirmDialog(null, "Deseja continuar?", "Atenção", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        JOptionPane.showMessageDialog(null, "Fim de Programa!");

    }

}
