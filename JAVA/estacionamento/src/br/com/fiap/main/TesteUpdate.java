package br.com.fiap.main;

import br.com.fiap.dao.CarroDAO;
import br.com.fiap.dao.ConnectionFactory;
import br.com.fiap.dto.Carro;

import java.sql.Connection;

public class TesteUpdate {
    public static void main(String[] args) {
        Connection con = ConnectionFactory.abrirConexao();

        Carro carro = new Carro();
        carro.setPlaca("ELL9244");
        carro.setCor("Vermelho");
        carro.setDescricao("Fiat Sienna");

        CarroDAO carroDAO = new CarroDAO(con);
        System.out.println(carroDAO.alterar(carro));

        ConnectionFactory.fecharConexao(con);
    }
}
