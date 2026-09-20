
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate
from app.models.movimentacao import MovimentacaoEstoque
from app.schemas.movimentacao import MovimentacaoCreate
from app.schemas.venda import VendaCreate
from app.models.venda import Venda
from app.models.item_venda import ItemVenda

Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def inicio():
    return {
        "mensagem": "Sistema da loja funcionando!"
    }

@app.post("/produtos")
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    novo_produto = Produto(
        nome=produto.nome,
        preco_custo= produto.preco_custo,
        preco_venda=produto.preco_venda,
        quantidade=produto.quantidade
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()

    return produtos

@app.get("/produtos/{produto_id}")
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if produto is None:
        raise HTTPException(status_code=404,detail="Produto não encontrado")
    return produto

@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto_atualizado: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if produto is None:
        return {
            "mensagem": "Produto não encontrado"
        }

    produto.nome = produto_atualizado.nome
    produto.preco_custo = produto_atualizado.preco_custo
    produto.preco_venda = produto_atualizado.preco_venda

    db.commit()
    db.refresh(produto)

    return produto

@app.delete("/produtos/{produto_id}")
def excluir_produto(
    produto_id:int,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id).first()

    if produto is None:
        return {
            "mensagem": "Produto não encontrado"
        }

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto excluido com sucesso"
    }

@app.post("/estoque/movimentacoes")
def criar_movimentacao(movimentacao: MovimentacaoCreate,db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(
        Produto.id == movimentacao.produto_id
    ).first()

    if produto is None:
        raise HTTPException(status_code=404,detail="Produto não encontrado")

    nova_movimentacao = MovimentacaoEstoque(
        produto_id=movimentacao.produto_id,
        tipo=movimentacao.tipo.value,
        quantidade=movimentacao.quantidade,
        motivo=movimentacao.motivo
    )

    if movimentacao.tipo.value == "entrada":
        produto.quantidade += movimentacao.quantidade

    elif movimentacao.tipo.value == "saida":
        if produto.quantidade < movimentacao.quantidade:
            raise HTTPException(status_code=400,detail="Estoque insuficiente")

        produto.quantidade -= movimentacao.quantidade

   
    db.add(nova_movimentacao)
    db.commit()
    db.refresh(nova_movimentacao)

    return nova_movimentacao

@app.get("/estoque/movimentacoes")
def listar_movimentacoes(db: Session = Depends(get_db)):
    movimentacoes = db.query(
        MovimentacaoEstoque
    ).all()

    resultado = []

    for movimentacao in movimentacoes:
        resultado.append({
            "id": movimentacao.id,
            "produto_id": movimentacao.produto_id,
            "produto_nome": movimentacao.produto.nome,
            "tipo": movimentacao.tipo,
            "quantidade": movimentacao.quantidade,
            "motivo": movimentacao.motivo,
            "data_hora": movimentacao.data_hora
        })

    return resultado

@app.post("/vendas")
def criar_venda(
    venda: VendaCreate,
    db: Session = Depends(get_db)
):
    valor_total = 0
    itens_venda = []

    for item in venda.itens:
        produto = db.query(Produto).filter(
            Produto.id == item.produto_id
        ).first()

        if produto is None:
            raise HTTPException(status_code=404, detail=f"Produto {item.produto_id} não encontrado")

        if produto.quantidade < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para o produto '{produto.nome}'")

        preco_unitario = produto.preco_venda
        subtotal = preco_unitario * item.quantidade

        valor_total += subtotal

        itens_venda.append({
            "produto": produto,
            "quantidade": item.quantidade,
            "preco_unitario": preco_unitario,
            "subtotal": subtotal
        })

    nova_venda = Venda(
        valor_total=valor_total
    )

    db.add(nova_venda)
    db.flush()

    for item in itens_venda:

        produto = item["produto"]

        produto.quantidade -= item["quantidade"]

        novo_item = ItemVenda(
            venda_id=nova_venda.id,
            produto_id=produto.id,
            quantidade=item["quantidade"],
            preco_unitario=item["preco_unitario"],
            subtotal=item["subtotal"]
        )

        db.add(novo_item)

        movimentacao = MovimentacaoEstoque(
            produto_id=produto.id,
            tipo="saida",
            quantidade=item["quantidade"],
            motivo=f"Venda #{nova_venda.id}"
        )

        db.add(movimentacao)

    db.commit()
    db.refresh(nova_venda)

    return nova_venda
    