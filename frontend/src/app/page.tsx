'use client';
import React, { useState } from 'react';

interface VerseResult {
  book: string;
  chapter: number;
  verse: number;
  text: string;
}

export default function BibleSearchPortal() {
  const [searchString, setSearchString] = useState('');
  const [results, setResults] = useState<VerseResult[]>([]);
  const [loading, setLoading] = useState(false);

  const executeSecureSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchString.trim()) return;

    setLoading(true);
    try {
      const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiBaseUrl}/api/search/?q=${encodeURIComponent(searchString)}`);

      if (!response.ok) throw new Error("API handshake failed.");
      const payload = await response.json();
      setResults(payload);
    } catch (err) {
      console.error("[ERROR] Network failure: ", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-900 text-slate-100 p-8">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="border-b border-slate-800 pb-4">
          <h1 className="text-2xl font-bold tracking-tight">KJV Bible Visualization Portal</h1>
        </header>

        <form onSubmit={executeSecureSearch} className="flex gap-2">
          <input
            type="text"
            placeholder="Search scripture parameters (e.g., 'light')..."
            value={searchString}
            onChange={(e) => setSearchString(e.target.value)}
            className="flex-1 bg-slate-950 border border-slate-800 rounded px-4 py-2 text-sm text-white focus:outline-none"
          />
          <button type="submit" className="bg-blue-600 hover:bg-blue-500 font-medium px-6 py-2 rounded text-sm">
            {loading ? 'Searching...' : 'Search'}
          </button>
        </form>

        <div className="space-y-4">
          {results.length > 0 ? (
            results.map((item, index) => (
              <div key={index} className="bg-slate-950 border border-slate-800 rounded p-4">
                <span className="text-xs font-mono text-blue-400">
                  {item.book} {item.chapter}:{item.verse}
                </span>
                <p className="text-sm text-slate-300 mt-2">{item.text}</p>
              </div>
            ))
          ) : (
            !loading && <p className="text-sm text-slate-500 text-center py-8">No results found.</p>
          )}
        </div>
      </div>
    </main>
  );
}
