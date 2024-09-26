package br.com.fiap.controller;

import br.com.fiap.model.dao.ConnectionFactory;
import br.com.fiap.model.dao.FilmeDAO;
import br.com.fiap.model.dto.Filme;

import java.sql.Connection;
import java.util.ArrayList;

public class FilmeController {

    public String inserirFilme(int codigo, String titulo, String genero, String produtora) {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Filme filme = new Filme();
        filme.setCodigo(codigo);
        filme.setTitulo(titulo);
        filme.setGenero(genero);
        filme.setProdutora(produtora);

        FilmeDAO filmeDAO = new FilmeDAO(con);
        resultado = filmeDAO.inserir(filme);

        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String alterarFilme(int codigo, String titulo, String genero, String produtora) {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Filme filme = new Filme();
        filme.setCodigo(codigo);
        filme.setTitulo(titulo);
        filme.setGenero(genero);
        filme.setProdutora(produtora);

        FilmeDAO filmeDAO = new FilmeDAO(con);
        resultado = filmeDAO.alterar(filme);

        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String excluirFilme(int codigo) {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Filme filme = new Filme();
        filme.setCodigo(codigo);

        FilmeDAO filmeDAO = new FilmeDAO(con);
        resultado = filmeDAO.excluir(filme);

        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String listarTodos() {

        String resultado = "";

        Connection con = ConnectionFactory.abrirConexao();

        Filme filme = new Filme();
        FilmeDAO filmeDAO = new FilmeDAO(con);
        ArrayList<Object> listaFilmes = filmeDAO.listarTodos(filme);


        if (listaFilmes != null && !listaFilmes.isEmpty()) {

            for (Object object : listaFilmes) {

                Filme filme1 = (Filme) object;

                resultado +=

                        "Código: " + filme1.getCodigo() +
                        "\nTítulo: " + filme1.getTitulo() +
                        "\nGênero: " + filme1.getGenero() +
                        "\nProdutora: " + filme1.getProdutora() +
                        "\n\n\n";

            }

        } else {

            resultado = "Nenhum filme encontrado.";

        }

        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String listarUmFilme(int codigo) {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Filme filme = new Filme();
        filme.setCodigo(codigo);

        FilmeDAO filmeDAO = new FilmeDAO(con);
        resultado = filmeDAO.listarUm(filme);

        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

}
