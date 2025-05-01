"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full px-6 py-4 bg-gradient-to-r from-[#0f0c29] to-[#302b63] flex justify-between items-center">
      {/* Logo */}
      <div className="flex items-center gap-2">

        <span className="text-white font-bold text-lg">
          <span className="text-white">PIXEL</span>
          <span className="text-purple-400">NFT💲</span>
        </span>
      </div>



      {/* Actions */}
      <div className="flex gap-3">
        <button className="flex items-center gap-2 px-4 py-1.5 bg-black text-white rounded-md border border-white text-sm hover:bg-white hover:text-black transition">
          💸 Connect Wallet
        </button>
        <button className="px-4 py-1.5 bg-purple-500 text-white rounded-md text-sm hover:bg-purple-600 transition">
          Sign In
        </button>
      </div>
    </nav>
  );
}
