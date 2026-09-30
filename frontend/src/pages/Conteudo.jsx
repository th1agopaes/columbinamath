import { useParams } from 'react-router-dom'

function Conteudo(){
    const { id } = useParams()

    const conteudos = {
        porcentagem: {
            titulo:'Porcentagem',
        },
        juros: {
            titulo: 'Juros simples e compostos',
        },
        'notacao-cientifica': {
            titulo: 'Potências de 10 e notação científica',
        },
    }

    const conteudo = conteudos[id]

    if (!conteudo){
        return(
            <main>
                <h1>Conteúdo não encontrado.</h1>
            </main>
        )
    }

    return(
        <main>
            <h1>{conteudo.titulo}</h1>
        </main>
    )
}

export default Conteudo