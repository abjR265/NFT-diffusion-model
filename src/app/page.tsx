'use client';

import { useState } from 'react';

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async () => {
    setLoading(true);
    setImageUrl('');
    setError('');

    try {
      const res = await fetch('https://nft-diffusion-model.vercel.app/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!res.ok) {
        throw new Error('Failed to generate image');
      }

      const data = await res.json();
      setImageUrl(data.image_url); // assumes Flask returns {"image_url": "..."}

    } catch (err: any) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white px-6 py-10">
      <h1 className="text-4xl font-bold mb-6">🧠 AI NFT Generator</h1>
      <p className="text-gray-300 mb-4 text-center max-w-xl">
        Enter a creative prompt below to generate an AI-powered NFT using our diffusion model.
      </p>

      <div className="flex w-full max-w-md gap-2 mb-4">
        <input
          type="text"
          className="flex-grow p-2 rounded bg-gray-800 border border-gray-600 text-white"
          placeholder="e.g. cyberpunk astronaut in neon city"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <button
          onClick={handleGenerate}
          className="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded text-white"
          disabled={loading || !prompt}
        >
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </div>

      {error && <p className="text-red-500 mt-2">{error}</p>}

      {imageUrl && (
        <div className="mt-6">
          <img
            src={imageUrl}
            alt="Generated NFT"
            className="max-w-full rounded-lg border border-gray-700"
          />
        </div>
      )}
    </main>
  );
}
