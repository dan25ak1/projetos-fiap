package br.com.fiap.dao;

import br.com.fiap.dto.Carro;
import br.com.fiap.dto.Cliente;

import java.sql.Connection;
import java.sql.PreparedStatement;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class ClienteDAO {
    private Connection con;

    public ClienteDAO(Connection con) {
        this.con = con;
    }

    public Connection getCon() {
        return con;
    }

    public String inserir(Cliente cliente) {
        String sql = "insert into ddd_cliente(id_cliente, nome_cliente, placa) values(?,?,?)"; // numero de interrogaçoes de acordo com colunas que queremos preencher
        try(PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setInt(1, cliente.getIdCliente());
            ps.setString(2, cliente.getNomeCliente());
            ps.setString(3, cliente.getPlaca());
            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso!";
            } else {
                return "Erro ao inserir!";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }
    public String alterar(Cliente cliente) {
        String sql = "update ddd_cliente  set NomeCliente=?, where placa=?"; // numero de interrogaçoes de acordo com colunas que queremos preencher
        try(PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setString(1, cliente.getNomeCliente());

            if (ps.executeUpdate() > 0) {
                return "Alterado com sucesso!";
            } else {
                return "Erro ao alterar!";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }
    public String excluir(Cliente cliente) {
        String sql = "delete from ddd_cliente where placa=?"; // numero de interrogaçoes de acordo com colunas que queremos preencher
        try(PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setString(1, cliente.getPlaca());
            if (ps.executeUpdate() > 0) {
                return "excluido com sucesso!";
            } else {
                return "Erro ao excluir!";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }
    public ArrayList<Cliente> listarTodos() {
        String sql = "select * from ddd_cliente order by placa";
        ArrayList<Cliente> listaCliente = new ArrayList<>();
        try(PreparedStatement ps = getCon().prepareStatement(sql);) {
            ResultSet rs = ps.executeQuery();
            if (rs != null){
                while(rs.next()){ //next é um metodo que le todas as linhas
                    Cliente cliente = new Cliente();
                    cliente.setIdCliente(rs.getInt(1));
                    cliente.setNomeCliente(rs.getString(2));
                    cliente.setPlaca(rs.getString(3));
                    listaCliente.add(cliente);
                }
                return listaCliente;
            }else {
                return null;
            }
        } catch (SQLException e) {
            System.out.println("Erro de SQL:" + e.getMessage());
            return null;
        }
    }
}
