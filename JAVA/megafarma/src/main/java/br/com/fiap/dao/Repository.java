package br.com.fiap.dao;

import java.sql.Connection;

public abstract class Repository {
    protected Connection connection;

    public Repository() {
    }

    public Connection getConnection() {
        try {
            connection = ConnectionFactory.getInstance().getConexao();
            return connection;
        } catch (Exception e) {
            System.out.println("Erro: "+ e.getMessage());
        }
        return null;
    }

    public void closeConnetcion() {
        try {
            if (connection.isClosed()) {
                connection.close();
            }
        } catch (Exception e) {
            System.out.println("Erro: "+ e.getMessage());
        }
    }

}
