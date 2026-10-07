import { Link } from 'react-router-dom'

// Barra de navegação que aparece em todas as páginas.
function Cabecalho() {
  return (
    <header className="cabecalho">
      <Link to="/" className="logo">
        Columbina<span>Math</span>
      </Link>
      <nav>
        <Link to="/conteudos">Conteúdos</Link>
      </nav>
    </header>
  )
}

export default Cabecalho
