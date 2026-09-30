import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home.jsx'
import Conteudos from './pages/Conteudos.jsx'
import Conteudo from './pages/Conteudo.jsx'
import './App.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/conteudos" element={<Conteudos />} />
      <Route path="/conteudos/:id" element={<Conteudo />} />
    </Routes>
  )
}

export default App