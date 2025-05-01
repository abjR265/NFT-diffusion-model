
"use client";

import { useState } from "react";
import Image from "next/image";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [meta, setMeta] = useState<any>(null);

  const generateNFT = async () => {
    setImageUrl("");
    setMeta(null);
    const res = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setImageUrl(data.image);
    setMeta(data);
  };

  return (
    <main className="bg-[#0b0b1c] text-white font-sans">
      {/* Hero */}
      <section className="min-h-screen flex flex-col items-center justify-center text-center px-6 py-24 bg-gradient-to-r from-[#0f0c29] to-[#302b63]">
        <h1 className="text-5xl sm:text-6xl font-bold mb-6 leading-tight">
        AI Diffusion-Based <br />
        <span className="text-purple-400">NFT Generator and Validator</span>
        </h1>
        <p className="text-lg max-w-xl text-gray-300 mb-10">
          Collect, trade, and create unique gaming NFTs. Own your in-game items across the metaverse with true digital ownership.
        </p>
        <div className="flex gap-4">
          <button className="bg-purple-500 text-white px-6 py-3 rounded-md hover:bg-purple-600 transition">
            Explore Collection
          </button>
          <button
            onClick={generateNFT}
            className="bg-black text-white px-6 py-3 rounded-md border border-white hover:bg-white hover:text-black transition"
          >
            Create NFT
          </button>
        </div>
        <div className="flex gap-8 mt-16 text-center text-sm sm:text-base">
          <div><span className="text-cyan-400 text-xl sm:text-2xl font-semibold">10K+</span><br />NFT Items</div>
          <div><span className="text-green-400 text-xl sm:text-2xl font-semibold">8.5K+</span><br />Artists</div>
          <div><span className="text-pink-400 text-xl sm:text-2xl font-semibold">12K+</span><br />Collectors</div>
        </div>
      </section>

      {/* What Are NFTs */}
      <section className="py-20 px-6 text-center bg-[#0e0e25]">
        <h2 className="text-4xl font-bold mb-4 text-blue-400">What Are NFTs?</h2>
        <p className="text-gray-300 mb-12 max-w-3xl mx-auto">
          Here’s everything you need to know about Non-Fungible Tokens and how they’re revolutionizing gaming.
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {[
            ["Unique Digital Assets", "NFTs are one-of-a-kind digital items that can’t be copied or taken away."],
            ["True Ownership", "Ownership is recorded on the blockchain like a digital deed."],
            ["Collect & Trade", "Build and trade rare items with others on marketplaces."],
            ["Use Across Games", "NFTs can be used across games that support them."]
          ].map(([title, desc], i) => (
            <div key={i} className="bg-[#181828] p-6 rounded-lg">
              <h3 className="text-lg font-semibold text-purple-300 mb-2">{title}</h3>
              <p className="text-sm text-gray-400">{desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="py-20 px-6 bg-[#101027] flex flex-col lg:flex-row items-center justify-between gap-12">
  {/* Text content */}
  <div className="flex-1 max-w-xl">
    <h2 className="text-3xl font-bold text-white mb-6">How Gaming NFTs Work</h2>
    <ol className="list-decimal text-left text-gray-300 space-y-3 pl-6">
      <li>Earn or purchase unique game items, characters, or land as NFTs</li>
      <li>Your ownership is recorded on the blockchain, making it secure</li>
      <li>Trade or sell NFTs on marketplaces when their value increases</li>
      <li>Use your NFTs across compatible games and platforms</li>
    </ol>
  </div>

  {/* YouTube video */}
  <div className="flex-1 w-full max-w-2xl">
    <div className="relative w-full pt-[56.25%]"> {/* 16:9 aspect ratio */}
      <iframe
        className="absolute top-0 left-0 w-full h-full rounded-xl"
        src="https://www.youtube.com/embed/MHGi76wUjUs"
        title="YouTube video"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      ></iframe>
    </div>
  </div>
</section>


      {/* Featured NFTs (placeholder) */}
      <section className="py-20 px-6 bg-[#0e0e22] text-center">
  <h2 className="text-3xl font-bold text-white mb-8">Featured NFTs</h2>
  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
    {[
      { name: "Cyber Samurai", src: "/cyber-samurai.png", price: "0.85", author: "NeoTokyo" },
      { name: "Dragon Guardian", src: "/dragon-guardian.png", price: "0.45", author: "PixelForge" },
      { name: "Space Explorer", src: "/space-explorer.png", price: "0.32", author: "CosmicArt" },
      { name: "Battle Mech", src: "/battlemech.png", price: "0.28", author: "TechWarrior" },
    ].map((nft, i) => (
      <div key={i} className="bg-[#1a1a2f] p-4 rounded-xl text-left">
        <Image
          src={nft.src}
          alt={nft.name}
          width={300}
          height={200}
          className="rounded mb-4 object-cover w-full h-40"
        />
        <h3 className="text-lg font-semibold text-white mb-1">{nft.name}</h3>
        <p className="text-sm text-gray-400">by {nft.author}</p>
        <div className="flex justify-between items-center mt-3">
          <span className="text-green-400 text-sm font-semibold">{nft.price} ETH</span>
          <button className="text-sm px-3 py-1 bg-purple-600 text-white rounded-md">View</button>
        </div>
      </div>
    ))}
  </div>
</section>

      {/* NFT Generator */}
      <section className="py-20 px-6 bg-[#0f0f1f] flex flex-col items-center text-center">
        <h2 className="text-3xl font-bold text-purple-400 mb-4">Create Your NFT</h2>
        <input
          type="text"
          placeholder="e.g. pixelated dragon breathing fire"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="w-full max-w-xl px-4 py-2 mb-4 bg-[#1c1c2b] text-white border border-gray-600 rounded"
        />
        <button
          onClick={generateNFT}
          className="bg-purple-600 text-white px-6 py-2 rounded hover:bg-purple-700 transition"
        >
          Generate NFT
        </button>
        {imageUrl && (
          <div className="mt-10">
            <Image src={imageUrl} alt="Generated NFT" width={300} height={300} />
            <p className="mt-4 text-sm text-gray-400">
              Similarity: {meta.similarity} | Prompt Match: {meta.prompt_match ? "✅" : "❌"} | Unique: {meta.is_unique ? "✅" : "❌"}
            </p>
          </div>
        )}
      </section>

    </main>
  );
}
