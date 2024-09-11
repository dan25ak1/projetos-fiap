package br.com.fiap.main;

import br.com.fiap.dao.ClienteDAO;
import br.com.fiap.dao.ConnectionFactory;
import br.com.fiap.dto.Cliente;

import java.sql.Connection;
import java.util.ArrayList;

public class TesteClienteCRUD {
    public static void main(String[] args) {
        Connection con = ConnectionFactory.abrirConexao();

        ClienteDAO clienteDAO = new ClienteDAO(con);
        Cliente cliente = new Cliente();
        // Inserindo 4 novos cliente
        cliente.setIdCliente(1);
        cliente.setNomeCliente("Danilo");
        cliente.setPlaca("ELL9244");
        System.out.println(clienteDAO.inserir(cliente));
        cliente.setIdCliente(2);
        cliente.setNomeCliente("Glerson");
        cliente.setPlaca("HKD1917");
        System.out.println(clienteDAO.inserir(cliente));
        cliente.setIdCliente(3);
        cliente.setNomeCliente("Perivaldo");
        cliente.setPlaca("ABC1234");
        System.out.println(clienteDAO.inserir(cliente));
        cliente.setIdCliente(4);
        cliente.setNomeCliente("Ludiene");
        cliente.setPlaca("YAG2424");
        System.out.println(clienteDAO.inserir(cliente));
        // Alterando os dados de um cliente
        cliente.setIdCliente(3);
        cliente.setNomeCliente("Penisvaldo");
        cliente.setPlaca("KKK2024");
        System.out.println(clienteDAO.alterar(cliente));
        // Excluindo um cliente
        cliente.setIdCliente(2);
        System.out.println(clienteDAO.excluir(cliente));
        // Listando todos os clientes
        ArrayList<Cliente> resultado = clienteDAO.listarTodos();
        if (resultado != null) {
            for (Cliente cliente1 : resultado){
                System.out.println("Id: " + cliente1.getIdCliente());
                System.out.println("Nome: " + cliente1.getNomeCliente());
                System.out.println("Placa: " + cliente1.getPlaca());
            }
        }


        ConnectionFactory.fecharConexao(con);
    }
}
