import { useState } from 'react'

// Um exercício de múltipla escolha com correção explicada.
// Recebe os dados do exercício (enunciado, alternativas, resolução)
// e o número dele na lista.
function Exercicio({ exercicio, numero }) {
  // "Estado" é a memória do componente. Quando ele muda, o React redesenha a tela.
  const [selecionada, setSelecionada] = useState(null) // índice da alternativa escolhida
  const [enviado, setEnviado] = useState(false) // a resposta já foi enviada?
  const [aviso, setAviso] = useState(false) // tentou enviar sem escolher?

  const indiceCorreto = exercicio.alternativas.findIndex((alt) => alt.correta)
  const acertou = selecionada === indiceCorreto

  function enviar(evento) {
    evento.preventDefault() // impede o navegador de recarregar a página
    if (selecionada === null) {
      setAviso(true) // não é erro matemático, só uma orientação
      return
    }
    setAviso(false)
    setEnviado(true)
  }

  function tentarNovamente() {
    setSelecionada(null)
    setEnviado(false)
  }

  return (
    <form className="exercicio" onSubmit={enviar}>
      <fieldset disabled={enviado}>
        <legend>
          <span className="exercicio-numero">Exercício {numero}</span>
          {exercicio.enunciado}
        </legend>

        <div className="alternativas">
          {exercicio.alternativas.map((alternativa, indice) => {
            // Depois do envio, pintamos a correta de verde e a escolhida errada de vermelho.
            let classe = 'alternativa'
            if (enviado && indice === indiceCorreto) classe += ' correta'
            if (enviado && indice === selecionada && !acertou) classe += ' incorreta'

            return (
              <label key={indice} className={classe}>
                <input
                  type="radio"
                  name={exercicio.id}
                  checked={selecionada === indice}
                  onChange={() => {
                    setSelecionada(indice)
                    setAviso(false)
                  }}
                />
                {alternativa.texto}
              </label>
            )
          })}
        </div>
      </fieldset>

      {/* aria-live faz leitores de tela anunciarem o resultado */}
      <div aria-live="polite">
        {aviso && <p className="aviso">Selecione uma alternativa antes de enviar.</p>}

        {enviado && (
          <div className={acertou ? 'resultado acerto' : 'resultado erro'}>
            <p className="resultado-titulo">
              {acertou ? 'Resposta correta! 🎉' : 'Resposta incorreta.'}
            </p>

            {!acertou && (
              <p className="feedback-erro">{exercicio.alternativas[selecionada].feedback}</p>
            )}

            <p>
              Alternativa correta: <strong>{exercicio.alternativas[indiceCorreto].texto}</strong>
            </p>

            <p className="resolucao-titulo">Resolução:</p>
            <ol className="passos">
              {exercicio.resolucao.map((passo) => (
                <li key={passo}>{passo}</li>
              ))}
            </ol>
          </div>
        )}
      </div>

      {enviado ? (
        <button type="button" className="botao secundario" onClick={tentarNovamente}>
          Tentar novamente
        </button>
      ) : (
        <button type="submit" className="botao">
          Enviar resposta
        </button>
      )}
    </form>
  )
}

export default Exercicio
