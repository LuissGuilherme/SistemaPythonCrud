# CRUD Inserção De Artistas e Músicas 

Este projeto é um sistema de inserção de artistas e músicas. O sistema permite realizar o CRUD (Criar, Ler, Atualizar e Deletar) através de uma interface desktop ou via API.

## Funcionalidades do Sistema

O sistema usa de duas entidades: Artistas e Músicas.

### Interface Gráfica (GUI)

Ao executar o módulo visual, você pode:

  * **Adicionar Artistas/Música:** Adiciona as informações dos artistas (Nome, Gênero Musical,) e músicas (Nome, Duração, Reproduções e ID do artista) na lista.
  * **Atualizar Selecionado:** Atualiza a música selecionada com as informações desejadas.
  * **Excluir:** Retira os registros da lista e do banco de dados.

## Instalação e Dependências

O projeto utiliza bibliotecas do Python, além do **Flask**.

1.  **Clonar o repositório:**

    ```bash
    git clone https://github.com/LuissGuilherme/SistemaPythonCrud.git
    ```

2.  **Instale o Flask:**

    ```bash
    pip install flask
    ```
    
## Estrutura do Projeto

  * `main.py`: Necessário pra rodar a aplicação.
  * `gui.py`: Uso do Tkinter para aplicar a interface gráfica(Janela, Botões, Lista) .
  * `api.py`: Servidor Flask.
  * `db.py`: Gerenciar o banco de dados.
