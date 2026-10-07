import { Link, useParams } from 'react-router-dom'
import { buscarConteudo } from '../data/conteudos.js'
import Exercicio from '../components/Exercicio.jsx'
import NaoEncontrado from './NaoEncontrado.jsx'

function Exercicios() {
  const { id } = useParams()
  const conteudo = buscarConteudo(id)

  if (!conteudo || !conteudo.disponivel) {
    return <NaoEncontrado mensagem="Não há exercícios para este conteúdo." />
  }

  return (
    <main>
      <Link to={`/conteudos/${conteudo.id}`} className="voltar">
        ← Voltar à explicação
      </Link>
      <h1>Exercícios: {conteudo.titulo}</h1>
      <p className="subtitulo">
        Escolha uma alternativa e envie. Se errar, vamos mostrar qual foi o erro.
      </p>

      {conteudo.exercicios.map((exercicio, indice) => (
        <Exercicio key={exercicio.id} exercicio={exercicio} numero={indice + 1} />
      ))}

      <Link to={`/conteudos/${conteudo.id}`} className="voltar">
        ← Voltar à explicação
      </Link>
    </main>
  )
}

export default Exercicios
