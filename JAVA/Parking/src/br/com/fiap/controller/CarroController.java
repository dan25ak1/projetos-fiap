package br.com.fiap.controller;

import br.com.fiap.model.dao.CarroDAO;
import br.com.fiap.model.dao.ConnectionFactory;
import br.com.fiap.model.dto.Carro;

import java.sql.Connection;
import java.sql.SQLException;

public class CarroController {

    public String inserirCarro(String placa, String cor, String descricao) throws ClassNotFoundException, SQLException {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Carro carro = new Carro();
        carro.setPlaca(placa);
        carro.setCor(cor);
        carro.setDescricao(descricao);

        CarroDAO carroDAO = new CarroDAO(con);
        resultado = carroDAO.inserir(carro);

        // Feche a conexão ANTES do retorno, pois o return encera o algoritmo
        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String alterarCarro(String placa, String cor, String descricao) throws ClassNotFoundException, SQLException {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Carro carro = new Carro();
        carro.setPlaca(placa);
        carro.setCor(cor);
        carro.setDescricao(descricao);

        CarroDAO carroDAO = new CarroDAO(con);
        resultado = carroDAO.alterar(carro);

        // Feche a conexão ANTES do retorno, pois o return encera o algoritmo
        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String excluirCarro(String placa) throws ClassNotFoundException, SQLException {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Carro carro = new Carro();
        carro.setPlaca(placa);

        CarroDAO carroDAO = new CarroDAO(con);
        resultado = carroDAO.excluir(carro);

        // Feche a conexão ANTES do retorno, pois o return encera o algoritmo
        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

    public String listarUmCarro(String placa) throws ClassNotFoundException, SQLException {

        String resultado;

        Connection con = ConnectionFactory.abrirConexao();

        Carro carro = new Carro();
        carro.setPlaca(placa);

        CarroDAO carroDAO = new CarroDAO(con);
        resultado = carroDAO.listarUm(carro);

        // Feche a conexão ANTES do retorno, pois o return encera o algoritmo
        ConnectionFactory.fecharConexao(con);

        return resultado;

    }

}
