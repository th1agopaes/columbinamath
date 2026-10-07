import { Link } from 'react-router-dom'

function Home() {
  return (
    <main className="home">
      <h1>
        Revise a base da matemática, <span className="destaque">um passo de cada vez.</span>
      </h1>
      <p className="subtitulo">
        Explicações curtas, exemplos resolvidos e exercícios que mostram exatamente onde você
        errou. Feito para estudantes do Ensino Médio.
      </p>

      <Link to="/conteudos" className="botao">
        Começar a estudar
      </Link>

      <ol className="como-funciona">
        <li>
          <strong>Entenda</strong>
          <span>Leia a explicação e acompanhe um exemplo resolvido.</span>
        </li>
        <li>
          <strong>Pratique</strong>
          <span>Responda aos exercícios de múltipla escolha.</span>
        </li>
        <li>
          <strong>Aprenda com o erro</strong>
          <span>Veja qual erro você cometeu e a resolução completa.</span>
        </li>
      </ol>
    </main>
  )
}

export default Home
