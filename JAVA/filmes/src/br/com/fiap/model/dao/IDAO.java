package br.com.fiap.model.dao;

public interface IDAO {

    // Na interface coloca-se apena a assinatura do metodo
    public String inserir(Object object);

    public String alterar(Object object);

    public String excluir(Object object);

    public String listarUm(Object object);

}
