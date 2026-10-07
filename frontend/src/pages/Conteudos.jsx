import { Link } from 'react-router-dom'
import { conteudos } from '../data/conteudos.js'

function Conteudos() {
  return (
    <main>
      <h1>Conteúdos</h1>
      <p className="subtitulo">
        Os conteúdos seguem uma trilha: cada um usa o que foi visto nos anteriores.
      </p>

      <ol className="lista-conteudos">
        {/* .map() transforma cada item da lista de dados em um elemento na tela */}
        {conteudos.map((conteudo, indice) => (
          <li key={conteudo.id}>
            {conteudo.disponivel ? (
              <Link to={`/conteudos/${conteudo.id}`} className="cartao">
                <span className="cartao-numero">{indice + 1}</span>
                <span className="cartao-texto">
                  <strong>{conteudo.titulo}</strong>
                  <span>{conteudo.descricao}</span>
                </span>
              </Link>
            ) : (
              <div className="cartao indisponivel" aria-disabled="true">
                <span className="cartao-numero">{indice + 1}</span>
                <span className="cartao-texto">
                  <strong>{conteudo.titulo}</strong>
                  <span>{conteudo.descricao}</span>
                </span>
                <span className="etiqueta">Em breve</span>
              </div>
            )}
          </li>
        ))}
      </ol>
    </main>
  )
}

export default Conteudos
