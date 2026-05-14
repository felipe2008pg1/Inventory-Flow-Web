let estoque = JSON.parse(localStorage.getItem('estoque')) || [];

function atualizarTela() {
    const corpoTabela = document.getElementById('corpo-tabela');
    const msgVazio = document.getElementById('mensagem-vazio');
    corpoTabela.innerHTML = '';

    if (estoque.length === 0) {
        msgVazio.classList.remove('hidden');
    } else {
        msgVazio.classList.add('hidden');
        estoque.forEach((item, index) => {
            corpoTabela.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${item.produto}</td>
                    <td>R$ ${parseFloat(item.preco).toFixed(2)}</td>
                    <td><button class="btn-remover" onclick="removerProduto(${index})">Remover</button></td>
                </tr>
            `;
        });
    }
    localStorage.setItem('estoque', JSON.stringify(estoque));
}

function adicionarProduto() {
    const nome = document.getElementById('produto-nome').value.toUpperCase();
    const preco = document.getElementById('produto-preco').value;

    if (nome && preco) {
        estoque.push({ produto: nome, preco: preco });
        document.getElementById('produto-nome').value = '';
        document.getElementById('produto-preco').value = '';
        atualizarTela();
    } else {
        alert("Preencha todos os campos!");
    }
}

function removerProduto(index) {
    if (confirm(`Remover ${estoque[index].produto}?`)) {
        estoque.splice(index, 1);
        atualizarTela();
    }
}
function atualizarHora() {
    const agora = new Date();
    document.getElementById('data-hora').innerText = `🕐 | Data: ${agora.toLocaleString('pt-BR')}`;
}

setInterval(atualizarHora, 1000);
atualizarTela();
