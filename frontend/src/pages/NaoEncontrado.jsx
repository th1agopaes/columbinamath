import { Link } from 'react-router-dom'

// Página mostrada quando a URL não corresponde a nada (erro 404).
function NaoEncontrado({ mensagem = 'Esta página não existe.' }) {
  return (
    <main>
      <h1>Ops! Página não encontrada</h1>
      <p className="subtitulo">{mensagem}</p>
      <Link to="/conteudos" className="botao">
        Ver conteúdos
      </Link>
    </main>
  )
}

export default NaoEncontrado
