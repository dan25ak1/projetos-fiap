package br.com.fiap.model.dao;

import br.com.fiap.model.dto.Filme;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class FilmeDAO implements IDAO{
    private Connection con;
    private Filme filme;

    public Connection getCon() {
        return con;
    }

    public FilmeDAO(Connection con) {
        this.con = con;
    }

    public String inserir(Object object){
        filme = (Filme) object;
        String sql = "insert into ddd_filme(titulo, genero, produtora) values(?, ?, ?)";

        try (PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setString(1, filme.getTitulo());
            ps.setString(2, filme.getGenero());
            ps.setString(3, filme.getProdutora());

            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso!";
            } else {
                return "Erro ao inserir.";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }

    public String alterar(Object object){
        filme = (Filme) object;
        String sql = "update ddd_filme set titulo=?, genero=?, produtora=? where codigo=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setString(1, filme.getTitulo());
            ps.setString(2, filme.getGenero());
            ps.setString(3, filme.getProdutora());

            if (ps.executeUpdate() > 0) {
                return "Alterado com sucesso!";
            } else {
                return "Erro ao alterar.";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }

    public String excluir(Object object){
        filme = (Filme) object;
        String sql = "delete from ddd_filme where codigo=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setInt(1, filme.getCodigo());

            if (ps.executeUpdate() > 0) {
                return "Excluído com sucesso!";
            } else {
                return "Erro ao excluir.";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }

    public String listarUm(Object object){
        filme = (Filme) object;
        String sql = "select * from ddd_filme where=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql);) {
            ps.setInt(1, filme.getCodigo());
            ResultSet rs = ps.executeQuery();
            if (ps.executeUpdate() > 0) {
                return "ID: " + filme.getCodigo() + "\nTitulo: " + rs.getString("titulo")
                        + "\nGenero: " + rs.getString("genero")
                        + "\nProdutora: " + rs.getString("produtora");
            } else {
                return "Filme não encontrado.";
            }
        } catch (SQLException e) {
            return "Erro de SQL: " + e.getMessage();
        }
    }
}
