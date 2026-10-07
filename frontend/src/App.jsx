import { Routes, Route } from 'react-router-dom'
import Cabecalho from './components/Cabecalho.jsx'
import Home from './pages/Home.jsx'
import Conteudos from './pages/Conteudos.jsx'
import Conteudo from './pages/Conteudo.jsx'
import Exercicios from './pages/Exercicios.jsx'
import NaoEncontrado from './pages/NaoEncontrado.jsx'
import './App.css'

// Cada <Route> liga um endereço (path) a uma página (element).
function App() {
  return (
    <>
      <Cabecalho />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/conteudos" element={<Conteudos />} />
        <Route path="/conteudos/:id" element={<Conteudo />} />
        <Route path="/conteudos/:id/exercicios" element={<Exercicios />} />
        {/* "*" pega qualquer endereço que não bateu com os de cima */}
        <Route path="*" element={<NaoEncontrado />} />
      </Routes>
    </>
  )
}

export default App
