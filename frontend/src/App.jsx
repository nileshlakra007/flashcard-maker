import { useState } from 'react'
import './App.css'

function App() {
  const [file, setFile] = useState(null)
  const [flashcards, setFlashcards] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async () => {
    if (!file) return
    setLoading(true)
    setError(null)
    const formData = new FormData()
    formData.append('file', file)
    try {
      const res = await fetch('http://localhost:8000/generate-flashcards', {
        method: 'POST',
        body: formData,
      })
      if (!res.ok) throw new Error('Failed to generate flashcards')
      const data = await res.json()
      setFlashcards(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">AI Flashcard Generator</h1>
      <input type="file" accept=".pdf,.txt" onChange={e => setFile(e.target.files[0])} />
      <button className="bg-blue-500 text-white px-4 py-2 ml-2" onClick={handleSubmit}>Generate</button>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      <div className="mt-4 space-y-2">
        {flashcards.map((fc, idx) => (
          <div key={idx} className="border p-2">
            <p className="font-semibold">Q: {fc.question}</p>
            <p>A: {fc.answer}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App
