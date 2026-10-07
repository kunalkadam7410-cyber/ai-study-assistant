export default function DashboardPage() {
  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-5xl rounded-2xl bg-white p-8 shadow-soft">
        <h1 className="text-3xl font-bold">Study Dashboard</h1>
        <p className="mt-2 text-slate-600">Upload notes, generate quizzes, and study with AI-powered guidance.</p>

        <div className="mt-8 grid gap-6 md:grid-cols-2">
          <div className="rounded-xl border border-slate-200 p-5">
            <h2 className="text-lg font-semibold">Upload material</h2>
            <form className="mt-4 space-y-4">
              <input type="text" placeholder="Document title" className="w-full rounded-lg border border-slate-200 p-3" />
              <input type="file" className="w-full rounded-lg border border-slate-200 p-3" />
              <button type="submit" className="w-full rounded-lg bg-primary-600 px-4 py-3 font-medium text-white">Upload</button>
            </form>
          </div>

          <div className="rounded-xl border border-slate-200 p-5">
            <h2 className="text-lg font-semibold">Ask a question</h2>
            <textarea placeholder="Ask about your notes..." className="mt-4 h-32 w-full rounded-lg border border-slate-200 p-3" />
            <button className="mt-4 w-full rounded-lg bg-slate-900 px-4 py-3 font-medium text-white">Get answer</button>
          </div>
        </div>

        <div className="mt-8 grid gap-6 md:grid-cols-2">
          <div className="rounded-xl border border-slate-200 p-5">
            <h2 className="text-lg font-semibold">Generated flashcards</h2>
            <ul className="mt-4 space-y-3 text-slate-700">
              <li>• Define the central concept in one sentence.</li>
              <li>• List 3 key terms and meanings.</li>
              <li>• Explain one real-world example.</li>
            </ul>
          </div>

          <div className="rounded-xl border border-slate-200 p-5">
            <h2 className="text-lg font-semibold">Quiz preview</h2>
            <ul className="mt-4 space-y-3 text-slate-700">
              <li>• Which concept is most central to the chapter?</li>
              <li>• What is the strongest comparison between the terms?</li>
              <li>• Which example best demonstrates the process?</li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  );
}
