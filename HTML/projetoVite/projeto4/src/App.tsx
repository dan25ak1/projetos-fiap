import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import './App.css'
import HomePage from './pages/Home/Home'
import AboutPage from './pages/About/About'
import NotFoundPage from './pages/NotFoundPage/NotFoundPage'

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  )
}

export default App