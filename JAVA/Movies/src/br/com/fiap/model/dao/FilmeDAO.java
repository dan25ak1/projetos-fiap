package br.com.fiap.model.dao;

import br.com.fiap.model.dto.Filme;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class FilmeDAO implements IDAO {

    private Connection con;
    private Filme filme;


    public FilmeDAO(Connection con) {
        this.con = con;
    }

    public Connection getCon() {
        return con;
    }


    public String inserir(Object object) {

        filme = (Filme) object;
        String sql = "insert into ddd_filme(codigo,titulo,genero,produtora) values(?,?,?,?)";

        try (PreparedStatement ps = getCon().prepareStatement(sql)) {

            ps.setInt(1, filme.getCodigo());
            ps.setString(2, filme.getTitulo());
            ps.setString(3, filme.getGenero());
            ps.setString(4, filme.getProdutora());

            if (ps.executeUpdate() > 0) {

                return "\nInserido com sucesso!";

            } else {

                return "\nErro ao inserir!";

            }

        } catch (SQLException e) {

            return "\nErro de SQL: " + e.getMessage();

        }

    }

    public String alterar(Object object) {

        filme = (Filme) object;
        String sql = "update ddd_filme set titulo=?,genero=?,produtora=? where codigo=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql)) {

            ps.setInt(4, filme.getCodigo());
            ps.setString(1, filme.getTitulo());
            ps.setString(2, filme.getGenero());
            ps.setString(3, filme.getProdutora());

            if (ps.executeUpdate() > 0) {

                return "\nAlterado com sucesso!";

            } else {

                return "\nErro ao alterar!";

            }

        } catch (SQLException e) {

            return "\nErro de SQL: " + e.getMessage();

        }

    }

    public String excluir(Object object) {

        filme = (Filme) object;
        String sql = "delete from ddd_filme where codigo=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql)) {

            ps.setInt(1, filme.getCodigo());

            if (ps.executeUpdate() > 0) {

                return "\nExcluído com sucesso!";

            } else {

                return "\nErro ao excluir!";

            }

        } catch (SQLException e) {

            return "\nErro de SQL: " + e.getMessage();

        }

    }

    public ArrayList<Object> listarTodos(Object object) {

        filme = (Filme) object;
        String sql = "select * from ddd_filme order by codigo";

        ArrayList<Object> listaFilme = new ArrayList<Object>();

        try (PreparedStatement ps = getCon().prepareStatement(sql);) {

            ResultSet rs = ps.executeQuery();

            if (rs != null) {

                while (rs.next()) {

                    Filme filme = new Filme();
                    filme.setCodigo(rs.getInt(1));
                    filme.setTitulo(rs.getString(2));
                    filme.setGenero(rs.getString(3));
                    filme.setProdutora(rs.getString(4));

                    listaFilme.add(filme);

                }

                return listaFilme;

            } else {

                return null;

            }

        } catch (SQLException e) {

            System.out.println("\nErro de SQL: " + e.getMessage());

            return null;

        }

    }

    public String listarUm(Object object) {

        filme = (Filme) object;
        String sql = "select * from ddd_filme where codigo=?";

        try (PreparedStatement ps = getCon().prepareStatement(sql)) {

            ps.setInt(1, filme.getCodigo());
            ResultSet rs = ps.executeQuery();

            if (rs.next()) {

                return "Código: " + filme.getCodigo() + "\nTítulo: " + rs.getString("titulo") + "\nGênero: " + rs.getString("genero") + "\nProdutora: " + rs.getString("produtora");

            } else {

                return "\nRegistro não encontrado!";

            }

        } catch (SQLException e) {

            return "\nErro de SQL: " + e.getMessage();

        }

    }

}
