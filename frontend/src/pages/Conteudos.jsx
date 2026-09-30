import { Link } from 'react-router-dom'

function Conteudos(){
    return (
        <main>
            <h1>Conteúdos</h1>
            <p>Escolha um conteúdo para estudar.</p>

            <Link to="/conteudos/porcentagem">
                Porcentagem
            </Link>

            <Link to="/conteudos/juros">
                Juros simples e compostos
            </Link>

            <Link to="/conteudos/notacao-cientifica">
                Potência de 10 e notação científica
            </Link>
        </main>
    )
}

export default Conteudos