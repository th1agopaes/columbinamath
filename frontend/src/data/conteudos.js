// Fonte única de dados dos conteúdos do ColumbinaMath.
// Todas as páginas leem daqui: para adicionar ou corrigir um conteúdo,
// basta editar este arquivo (não é preciso mexer nas páginas).
//
// A ordem da lista segue a trilha de pré-requisitos:
// cada conteúdo depende dos anteriores.

export const conteudos = [
  {
    id: 'operacoes-basicas',
    titulo: 'Operações básicas',
    descricao: 'Adição, subtração, multiplicação e divisão com números naturais.',
    disponivel: true,
    introducao:
      'As quatro operações são a base de toda a matemática. Quase todo erro em conteúdos mais avançados começa com um tropeço aqui. Vamos revisar cada uma com calma, sempre conferindo o resultado com a operação inversa (a "prova real").',
    secoes: [
      {
        titulo: 'Adição',
        explicacao:
          'Adicionar é juntar quantidades. Os números somados são as parcelas e o resultado é a soma. Na conta armada, somamos coluna por coluna, da direita para a esquerda. Quando uma coluna passa de 9, escrevemos só a unidade e levamos o resto para a próxima coluna (o famoso "vai um").',
        exemplo: {
          conta: '158 + 276',
          passos: [
            'Unidades: 8 + 6 = 14. Escrevemos 4 e vai 1 para as dezenas.',
            'Dezenas: 5 + 7 + 1 (que veio) = 13. Escrevemos 3 e vai 1 para as centenas.',
            'Centenas: 1 + 2 + 1 (que veio) = 4. Escrevemos 4.',
          ],
          resultado: '158 + 276 = 434',
          provaReal: '434 − 276 = 158 ✔',
        },
      },
      {
        titulo: 'Subtração',
        explicacao:
          'Subtrair é tirar uma quantidade de outra. O número de cima é o minuendo, o que tiramos é o subtraendo e o resultado é a diferença. Se o algarismo de cima for menor que o de baixo, pegamos emprestado 1 da coluna da esquerda, que vale 10 na coluna atual.',
        exemplo: {
          conta: '432 − 157',
          passos: [
            'Unidades: 2 é menor que 7. Pegamos 1 emprestado das dezenas: 12 − 7 = 5.',
            'Dezenas: o 3 virou 2. Como 2 é menor que 5, pegamos 1 das centenas: 12 − 5 = 7.',
            'Centenas: o 4 virou 3. Então 3 − 1 = 2.',
          ],
          resultado: '432 − 157 = 275',
          provaReal: '275 + 157 = 432 ✔',
        },
      },
      {
        titulo: 'Multiplicação',
        explicacao:
          'Multiplicar é somar parcelas iguais repetidas vezes: 3 × 4 = 4 + 4 + 4. Os números multiplicados são os fatores e o resultado é o produto. Com dois algarismos no segundo fator, multiplicamos por partes (unidades e dezenas) e depois somamos.',
        exemplo: {
          conta: '34 × 12',
          passos: [
            'Separamos o 12 em 10 + 2.',
            'Multiplicamos pelas unidades: 34 × 2 = 68.',
            'Multiplicamos pelas dezenas: 34 × 10 = 340 (por isso a segunda linha da conta armada começa uma casa à esquerda).',
            'Somamos as partes: 68 + 340 = 408.',
          ],
          resultado: '34 × 12 = 408',
          provaReal: '408 ÷ 12 = 34 ✔',
        },
      },
      {
        titulo: 'Divisão',
        explicacao:
          'Dividir é repartir em partes iguais. O número dividido é o dividendo, o que divide é o divisor, o resultado é o quociente e o que sobra é o resto. Dividimos da esquerda para a direita, "baixando" um algarismo por vez. Atenção: se depois de baixar um algarismo o número ainda for menor que o divisor, escrevemos 0 no quociente.',
        exemplo: {
          conta: '156 ÷ 4',
          passos: [
            '1 é menor que 4, então pegamos 15.',
            '15 ÷ 4 = 3 (pois 3 × 4 = 12). Sobra 15 − 12 = 3.',
            'Baixamos o 6, formando 36.',
            '36 ÷ 4 = 9 (pois 9 × 4 = 36). Sobra 0.',
          ],
          resultado: '156 ÷ 4 = 39',
          provaReal: '39 × 4 = 156 ✔',
        },
      },
    ],
    // Cada alternativa errada representa um erro comum.
    // O campo "feedback" explica aquele erro específico.
    exercicios: [
      {
        id: 'adicao',
        enunciado: 'Quanto é 247 + 185?',
        alternativas: [
          {
            texto: '322',
            feedback: 'Você esqueceu de levar o "vai um" nas duas colunas. 7 + 5 = 12 e 4 + 8 = 12: nos dois casos, o 1 precisa ir para a coluna seguinte.',
          },
          { texto: '432', correta: true },
          {
            texto: '422',
            feedback: 'Você esqueceu o "vai um" das unidades. 7 + 5 = 12: escrevemos 2 e o 1 vai para as dezenas, que ficam 4 + 8 + 1 = 13.',
          },
          {
            texto: '332',
            feedback: 'Você esqueceu o "vai um" das dezenas. 4 + 8 + 1 = 13: escrevemos 3 e o 1 vai para as centenas, que ficam 2 + 1 + 1 = 4.',
          },
        ],
        resolucao: [
          'Unidades: 7 + 5 = 12. Escrevemos 2 e vai 1.',
          'Dezenas: 4 + 8 + 1 = 13. Escrevemos 3 e vai 1.',
          'Centenas: 2 + 1 + 1 = 4.',
          'Resultado: 432. Prova real: 432 − 185 = 247 ✔',
        ],
      },
      {
        id: 'subtracao',
        enunciado: 'Quanto é 503 − 268?',
        alternativas: [
          {
            texto: '365',
            feedback: 'Você subtraiu o menor do maior em cada coluna (8 − 3 e 6 − 0). Quando o algarismo de cima é menor, é preciso pegar emprestado da coluna da esquerda.',
          },
          {
            texto: '335',
            feedback: 'Você pegou emprestado, mas esqueceu de diminuir as centenas. Depois do empréstimo, o 5 vira 4, e 4 − 2 = 2.',
          },
          { texto: '235', correta: true },
          {
            texto: '245',
            feedback: 'Quase! Ao emprestar através do zero, as dezenas ficam com 9 (e não 10), porque 1 delas foi para as unidades. Então 9 − 6 = 3.',
          },
        ],
        resolucao: [
          'Unidades: 3 é menor que 8 e as dezenas são 0. Pegamos 1 das centenas: o 5 vira 4 e o 0 das dezenas vira 10.',
          'Das 10 dezenas, passamos 1 para as unidades: as dezenas ficam 9 e as unidades ficam 13.',
          'Unidades: 13 − 8 = 5. Dezenas: 9 − 6 = 3. Centenas: 4 − 2 = 2.',
          'Resultado: 235. Prova real: 235 + 268 = 503 ✔',
        ],
      },
      {
        id: 'multiplicacao',
        enunciado: 'Quanto é 23 × 14?',
        alternativas: [
          {
            texto: '115',
            feedback: 'Você não deslocou a segunda linha da conta armada. O 1 do 14 vale 10, então a segunda parte é 23 × 10 = 230 (e não 23).',
          },
          {
            texto: '212',
            feedback: 'Você multiplicou algarismo por algarismo (2 × 1 e 3 × 4). É preciso multiplicar o número 23 inteiro por cada parte do 14.',
          },
          {
            texto: '37',
            feedback: 'Você somou em vez de multiplicar (23 + 14 = 37). Leia o sinal com atenção: × é multiplicação.',
          },
          { texto: '322', correta: true },
        ],
        resolucao: [
          'Separamos o 14 em 10 + 4.',
          '23 × 4 = 92.',
          '23 × 10 = 230.',
          '92 + 230 = 322. Prova real: 322 ÷ 14 = 23 ✔',
        ],
      },
      {
        id: 'divisao',
        enunciado: 'Quanto é 612 ÷ 6?',
        alternativas: [
          { texto: '102', correta: true },
          {
            texto: '12',
            feedback: 'Você esqueceu o zero no quociente. Depois de 6 ÷ 6 = 1, baixamos o 1, que é menor que 6: nesse caso escrevemos 0 antes de continuar. Prova real: 12 × 6 = 72, não 612.',
          },
          {
            texto: '120',
            feedback: 'O zero foi para o lugar errado. Prova real: 120 × 6 = 720, não 612. O zero entra quando baixamos o 1 (que é menor que 6).',
          },
          {
            texto: '606',
            feedback: 'Você subtraiu em vez de dividir (612 − 6 = 606). Leia o sinal com atenção: ÷ é divisão.',
          },
        ],
        resolucao: [
          '6 ÷ 6 = 1. Sobra 0.',
          'Baixamos o 1. Como 1 é menor que 6, escrevemos 0 no quociente.',
          'Baixamos o 2, formando 12. 12 ÷ 6 = 2. Sobra 0.',
          'Resultado: 102. Prova real: 102 × 6 = 612 ✔',
        ],
      },
    ],
  },
  // Conteúdos planejados (aparecem como "Em breve" na listagem).
  {
    id: 'regra-de-sinais',
    titulo: 'Regra de sinais',
    descricao: 'Operações com números negativos.',
    disponivel: false,
  },
  {
    id: 'ordem-das-operacoes',
    titulo: 'Ordem das operações',
    descricao: 'Expressões numéricas com parênteses, potências e as quatro operações.',
    disponivel: false,
  },
  {
    id: 'fracoes',
    titulo: 'Frações',
    descricao: 'Simplificação e operações com frações.',
    disponivel: false,
  },
  {
    id: 'porcentagem',
    titulo: 'Porcentagem',
    descricao: 'Cálculo de porcentagens, aumentos e descontos.',
    disponivel: false,
  },
  {
    id: 'notacao-cientifica',
    titulo: 'Potências de 10 e notação científica',
    descricao: 'Como escrever números muito grandes ou muito pequenos.',
    disponivel: false,
  },
  {
    id: 'juros',
    titulo: 'Juros simples e compostos',
    descricao: 'Como o dinheiro cresce ao longo do tempo.',
    disponivel: false,
  },
]

// Procura um conteúdo pelo id da URL. Retorna undefined se não existir.
export function buscarConteudo(id) {
  return conteudos.find((conteudo) => conteudo.id === id)
}
