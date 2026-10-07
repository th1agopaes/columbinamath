import { Link, useParams } from 'react-router-dom'
import { buscarConteudo } from '../data/conteudos.js'
import NaoEncontrado from './NaoEncontrado.jsx'

function Conteudo() {
  const { id } = useParams() // pega o pedaço ":id" da URL
  const conteudo = buscarConteudo(id)

  if (!conteudo) {
    return <NaoEncontrado mensagem="Este conteúdo não existe." />
  }

  if (!conteudo.disponivel) {
    return (
      <main>
        <h1>{conteudo.titulo}</h1>
        <p className="subtitulo">Este conteúdo ainda está sendo preparado. Volte em breve!</p>
        <Link to="/conteudos" className="voltar">← Voltar aos conteúdos</Link>
      </main>
    )
  }

  return (
    <main>
      <Link to="/conteudos" className="voltar">← Voltar aos conteúdos</Link>
      <h1>{conteudo.titulo}</h1>
      <p className="subtitulo">{conteudo.introducao}</p>

      {conteudo.secoes.map((secao) => (
        <section key={secao.titulo} className="secao">
          <h2>{secao.titulo}</h2>
          <p>{secao.explicacao}</p>

          <div className="exemplo">
            <p className="exemplo-titulo">
              Exemplo resolvido: <span className="conta">{secao.exemplo.conta}</span>
            </p>
            <ol className="passos">
              {secao.exemplo.passos.map((passo) => (
                <li key={passo}>{passo}</li>
              ))}
            </ol>
            <p className="conta resultado-exemplo">{secao.exemplo.resultado}</p>
            <p className="prova-real">Prova real: {secao.exemplo.provaReal}</p>
          </div>
        </section>
      ))}

      <div className="chamada">
        <p>Entendeu? Agora é hora de praticar!</p>
        <Link to={`/conteudos/${conteudo.id}/exercicios`} className="botao">
          Ir para os exercícios
        </Link>
      </div>
    </main>
  )
}

export default Conteudo
