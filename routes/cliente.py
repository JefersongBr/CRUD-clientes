from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint("cliente", __name__)

@cliente_route.route("/")
def lista_clientes():
    return render_template("lista_clientes.html", clientes=CLIENTES)


@cliente_route.route("/", methods=["POST"])
def criar_clientes():

    data = request.json

    novo_cliente = {
        "id": len(CLIENTES) + 1,  
        "nome": data.get("nome"),
        "email": data.get("email"),
    }

    CLIENTES.append(novo_cliente)

    return render_template("item_cliente.html", cliente=novo_cliente)


@cliente_route.route("/new")
def form_cliente():
    return render_template("form_cliente.html")


@cliente_route.route("/<int:cliente_id>")
def detalhe_cliente(cliente_id):
    return render_template("detalhe_cliente.html", cliente_id=cliente_id)


@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):
    
    cliente = None
    for c in CLIENTES:
        if c["id"] == cliente_id:
            cliente = c
            break

    return render_template("form_cliente.html", cliente_id=cliente_id)


@cliente_route.route("/<int:cliente_id>/update", methods=["PUT"])
def atualizar_cliente(cliente_id):
    pass


@cliente_route.route("/<int:cliente_id>/delete", methods=["DELETE"])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c["id"] != cliente_id]
    return "deleted: sucess"